from elements.code_segment import Block
from elements.line import Line
from utils.config import FILENAME


class Parser:

    def __init__(self, file):
        f = open(file, "r")
        self.data = ""
        for line in f.readlines():
            cleaned_line = line.strip()
            if cleaned_line != "" and cleaned_line[0] == "#":
                pass
            else:
                self.data += cleaned_line
        f.close()

        self.blocks = self.blockify(self.parse_to_blocks(self.data))

    def parse_to_blocks(self, string):
        """Parse raw string to blocks

        creates multidimensional list from source code given as a parameter.
        code is splitted on every ; character and { } defines dimension.

        method also tries to strip off unnecessary whitespace

        :param string: code, String
        :return: Multidimensional list of strings
        """
        data = string
        blocks = []
        while data != "":
            open_index = None
            close_index = None
            if "{" in data:
                open_index = data.index("{")
            if "}" in data:
                close_index = data.index("}")

            if open_index is not None and open_index < close_index:
                splitted_data = data.split("{", 1)
                for line in splitted_data[0].split(";"):
                    blocks.append(line.strip())
                returned_blocks, remaining = self.parse_to_blocks(splitted_data[1])
                blocks.append(returned_blocks)
                data = remaining
            elif close_index is not None:
                splitted_data = data.split("}", 1)
                for line in splitted_data[0].split(";"):
                    blocks.append(line.strip())
                remaining = splitted_data[1]
                return blocks, remaining
            else:
                blocks.append(data)
                data = ""

        blocks = self.clear_emptys(blocks)
        return blocks

    def clear_emptys(self, data):
        """Clear empty strings

        recursively clears all empty strings from multidimensional list.

        :param data: Multidimensional list containing strings
        :return: Multidimensional list containing strings
        """
        clear_data = []
        for i in range(0, len(data)):
            if type(data[i]) == str:
                if data[i] != "":
                    clear_data.append(data[i])
            else:
                returned_data = self.clear_emptys(data[i])
                if len(returned_data) > 0:
                    clear_data.append(returned_data)
        return clear_data

    def blockify(self, blocks):
        """Get block elements

        Turns mutidimensionla list to elements.block.Block style
        Blocks.

        :param blocks: multidimensional list
        :return: Block
        """
        element_list = []
        for element in blocks:
            if type(element) == str:
                element_list.append(Line(element))
            else:
                new_block = self.blockify(element)
                if element_list and element_list[-1].is_pre_block():
                    element_list[-1].command.set_block(new_block)
                else:
                    element_list.append(new_block)
        block = Block()
        block.add_element_list(element_list)
        return block

    def write_out(self):
        print(self.blocks)

def read_file(path: str) -> str:
    """Read file

    reads the file in path stripping all leading and trailing
    whitespace from every line and returns all it's contents
    in one, single line string.

    :param path: /path/to/file
    :return: file as a string
    """
    string = ""
    with open(path) as f:
        for l in f.readlines():
            string += l.strip()
    return string

def get_hierarchy(string: str) -> list:
    """Get hierarchy

    Parses given string and returns a hierarchic list
    based on normal and curly parentheses found in in it.

    Example:
    >>> get_hierarchy("abc(d{ef})g")
    ['abc', ['d', ['ef']], 'g']

    :param string: string
    :return: list
    """
    hl = [] # hierarchy list
    i = 0   # index
    d = 0   # depth
    ts = "" # temp string
    for i in range(len(string)):
        c = string[i]
        if d < 0:
            break
        elif c in ("(", "{"):
            if d == 0:
                hl.append(ts)
                ts = ""
                hl.append(get_hierarchy(string[i+1:]))
            d += 1
        elif c in (")", "}"):
            d -= 1
        elif d == 0:
            ts += c
        else:
            pass
    if ts:
        hl.append(ts)
    return hl



if __name__ == "__main__":

    a = Parser(FILENAME).blocks
    print("#### BSQF")
    print(a.write_out())
    print("#### SQF")
    print(a.write_sqf())
