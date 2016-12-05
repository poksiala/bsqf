from elements.code_elements import GenericElement, VariableElement
from elements.code_segment import CodeSegment
from elements.datatype_elements import StringElement, NumberElement
from utils.commands import COMMANDS, TWO_SIDED_COMMANDS, NO_PARAM_COMMANDS, ALL_COMMANDS, PRE_BLOCK_COMMANDS
from utils.util import flatten


class Line(CodeSegment):

    def __init__(self, string: str):
        """Line

        Represents single line of code. Contains
        information about parent

        :param string: code line, String
        """
        self.command = parse_line(string)
        self.parent = None
        self.command.set_parent(self)

    def write_out(self, sqf=False):
        """Write out

        returns line contents with ; added to the end.

        :return: String
        """
        if sqf:
            string = self.command.write_sqf()
        else:
            string = self.command.write_out()
        if self.is_pre_block():
            return self.indent() + string
        else:
            return self.indent() + string + ";\n"

    def is_pre_block(self):
        if isinstance(self.command, PRE_BLOCK_COMMANDS):
            return True
        else:
            return False


def parse_line(string: str) -> GenericElement:
    """Parse line to command

    Parses line contents and turns it to
    element.code_elements.GenericElement's
    subclass instance.

    :param string: str
    :return: Command
    """
    segmented_line = divide_into_segments(string)
    mixed_list = get_literal_elements(segmented_line)
    hierarchy = get_hierarchy(mixed_list)
    command = flatten(get_commands(hierarchy))[0]
    return command


def get_hierarchy(segment_list: list) -> list:
    """Get hierarchy

    Method goes trough the list given as a parameter
    and parses it to multidimensional list based on "("
    and ")" cells found in it.

    example ["a", "(", "b", ")", "c"] would return
    the following: ["a", ["b"], "c"]

    :param segment_list: One dimensional list
    :return: Multidimensional list
    """
    element_list = []
    index = 0
    in_sublist = 0
    while index < len(segment_list):
        if in_sublist == 0:
            if segment_list[index] == "(":
                in_sublist += 1
                returned_list = get_hierarchy(segment_list[index+1:])
                element_list.append(returned_list)
            elif segment_list[index] == ")":
                return element_list
            else:
                element_list.append(segment_list[index])

        elif segment_list[index] == "(":
            in_sublist += 1
        elif segment_list[index] == ")":
            in_sublist -= 1
        else:
            pass
        index += 1
    return element_list


def get_commands(hl: list):
    # TODO: Special case =
    # TODO: Maths: order of computation
    i = 0
    command_list = []
    while i < len(hl):

        if type(hl[i]) is list:
            command_list.append(get_commands(hl[i]))
        elif type(hl[i]) is str:
            if hl[i] in COMMANDS.keys():
                command_list.append(create_command(hl[i], get_commands(hl[i+1])))
                i += 1
            elif hl[i] in TWO_SIDED_COMMANDS.keys():
                asd = hl[i]
                if isinstance(hl[i+1], GenericElement):
                    right = hl[i+1]
                elif type(hl[i+1]) is list:
                    right = get_commands(hl[i+1])
                else:
                    right = get_commands(hl[i+1:])
                    i = len(hl)
                command_list.append(
                    create_math_command(asd,
                                        command_list.pop(),
                                        right))
                i += 1
            elif hl[i] in NO_PARAM_COMMANDS.keys():
                command_list.append(
                    NO_PARAM_COMMANDS[hl[i]]()
                )
                i += 1
            else:
                command_list.append(hl[i])
        else:
            command_list.append(hl[i])

        i += 1
    return command_list


def divide_into_segments(string: str) -> list:
    """Divide string to segments

    Method divides given string to logical code segments
    starting from left to right.

    example: '"asd"+(random(1,5) == var123)'
    would produce: ", asd, ", +, (, random, (, 1, 5, ), ==, var123, )

    :param string: str
    :return: list
    """
    operators = ["=", "!", "<", ">", "|", "&"]
    segment_list = []
    looking_for = None
    start = -1
    end = False
    for i in range(len(string)):
        if looking_for == "int":
            if not string[i].isdigit():
                end = i
        if looking_for == "str":
            if not string[i].isalnum():
                end = i
        if looking_for == "operator":
            if not string[i] in operators:
                end = i
        elif looking_for == "pass":
            end = i

        if end:
            segment = string[start: end]
            segment_list.append(segment)
            end = False
            looking_for = None

        if looking_for is None:
            start = i
            if string[i].isspace() or string[i] == ",":
                start = -1
            elif string[i].isdigit():
                looking_for = "int"
            elif string[i].isalpha():
                looking_for = "str"
            elif string[i] in operators:
                looking_for = "operator"
            else:
                looking_for = "pass"

    if looking_for is not None:
        segment_list.append(string[start:])

    return segment_list


def get_literal_elements(segment_list: list) -> list:
    """Get literal elements

    Method goes trough list and forms string and num literals
    as well as variables.

    -   String literals are limited by " (' doesnt work)
    -   Num literals are segments only containing digits.
        decimals are not yet supported.
    -   Variables are alphanumeric segments that don't
        match to any supported commands

    :param segment_list: list
    :return: list
    """
    # get string elements
    new_list = []
    to_be_joined = []
    in_string = False
    for segment in segment_list:
        if segment == '"':
            if not in_string:
                in_string = True
            else:
                in_string = False
                new_list.append(StringElement(' '.join(to_be_joined)))
                to_be_joined = []
        elif not in_string:
            new_list.append(segment)
        else:
            to_be_joined.append(segment)

    # get number elements and variables
    another_list = []
    for segment in new_list:
        if type(segment) is str:
            if segment.isdigit():
                another_list.append(NumberElement(segment))
            elif segment.isalnum() and segment not in ALL_COMMANDS.keys():
                another_list.append(VariableElement(segment))
            else:
                another_list.append(segment)
        else:
            another_list.append(segment)

    return another_list


def create_command(command: str, params):

    args = flatten(params)
    try:
        return COMMANDS[command](*args)
    except TypeError:
        print("### ERROR WHILE:")
        print("creating command: {}({})".format(str(command), str(args)))


def create_math_command(command: str, left, right):
    args = flatten([left, right])
    try:
        return TWO_SIDED_COMMANDS[command](*args)
    except TypeError:
        print("### ERROR WHILE:")
        print("creating math command: {} {} {}".format(str(args[0]), str(command), str(args[1])))
        print("all args: ", str(args))


if __name__ == "__main__":
    # For testing purposes
    test_lines = [
        'hint("asd")',
        'random(random(1, 2),random(4,5))',
        '1 + 2 + 3 + 4',
        '"asd" + "kek"',
        'random(((1))+(2),(((3))+(2)))',
        'random((1),((2)))'
    ]

    for line in test_lines:
        a = parse_line(line)
        print(a.write_sqf())
