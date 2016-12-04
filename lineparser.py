from utils.commands import COMMANDS, MATH_COMMANDS
from elements.datatype_elements import StringElement, NumberElement
from elements.code_elements import VariableElement, GenericElement
from utils.util import recursive_print, flatten

class LineParser:

    def __init__(self, line: str):
        #self.line = self.parse_line(line)
        self.segmented_line = self.divide_into_segments(line)
        self.mixed_list = self.get_literal_elements(self.segmented_line)
        self.hierarchy = self.get_hierarchy(self.mixed_list)
        self.command = self.get_commands(self.hierarchy)
    def parse_line(self):



        return None

    def divide_into_segments(self, line):
        operators = ["=", "!", "<", ">", "|", "&"]
        segment_list = []
        looking_for = None
        start = -1
        end = False
        for i in range(len(line)):
            if looking_for == "int":
                if not line[i].isdigit():
                    end = i
            if looking_for == "str":
                if not line[i].isalnum():
                    end = i
            if looking_for == "operator":
                if not line[i] in operators:
                    end = i
            elif looking_for == "pass":
                end = i

            if end:
                segment = line[start: end]
                segment_list.append(segment)
                end = False
                looking_for = None

            if looking_for is None:
                start = i
                if line[i].isspace() or line[i] == ",":
                    start = -1
                elif line[i].isdigit():
                    looking_for = "int"
                elif line[i].isalpha():
                    looking_for = "str"
                elif line[i] in operators:
                    looking_for = "operator"
                else:
                    looking_for = "pass"

        if looking_for is not None:
            segment_list.append(line[start:])

        return segment_list

    def get_literal_elements(self, segment_list: list):
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
                elif segment.isalnum() and segment.lower() not in COMMANDS.keys() \
                        and segment.lower() not in MATH_COMMANDS.keys():
                    another_list.append(VariableElement(segment))
                else:
                    another_list.append(segment)
            else:
                another_list.append(segment)

        return another_list

    def get_hierarchy(self, segment_list):
        element_list = []
        index = 0
        in_sublist = 0
        while index < len(segment_list):
            if in_sublist == 0:
                if segment_list[index] == "(":
                    in_sublist += 1
                    returned_list = self.get_hierarchy(segment_list[index+1:])
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

    def get_commands(self, hl: list):
        #print("\nget_commands:")
        #recursive_print(hl)
        i = 0
        command_list =[]
        while i < len(hl):

            if type(hl[i]) is list:
                command_list.append(self.get_commands(hl[i]))
            elif type(hl[i]) is str:
                if hl[i] in COMMANDS.keys():
                    command_list.append(self.create_command(hl[i], self.get_commands(hl[i+1])))
                    i += 1
                elif hl[i] in MATH_COMMANDS.keys():
                    right = None
                    asd = hl[i]
                    if isinstance(hl[i+1], GenericElement):
                        right = hl[i+1]
                    elif type(hl[i+1]) is list:
                        right = self.get_commands(hl[i+1])
                    else:
                        right = self.get_commands(hl[i+1:])
                        i = len(hl)
                    command_list.append(
                        self.create_math_command(asd,
                                             command_list.pop(),
                                             right))
                    i += 1

                else:
                    command_list.append(hl[i])
            else:
                command_list.append(hl[i])

            i+=1
        return command_list



    def create_command(self, command, params):
        args = flatten(params)
        print("creating command: {}({})".format(str(command), str(args)))
        return COMMANDS[command](*args)

    def create_math_command(self, command, left, right):
        args = flatten([left, right])

        print("creating math command: {} {} {}".format(str(args[0]), str(command), str(args[1])))

        return MATH_COMMANDS[command](*args)

    def write_out(self):
        return  self.command[0].write_out()


if __name__ == "__main__":
    test_lines = [
        #'hint("asd")',
        #'random(random(1, 2),random(4,5))',
        #'1 + 2 + 3 + 4',
        #'"asd" + "kek"',
        'random(((1))+(2),(((3))+(2)))',
        'random((1),((2)))'
    ]

    for line in test_lines:
        a = LineParser(line).command
        print("#######")
        print(a)
        recursive_print(a)