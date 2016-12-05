from elements.code_elements import CodeSegment
from lineparser import LineParser
from utils.util import is_pre_block_command
class Line(CodeSegment):

    def __init__(self, line):
        """Line

        Represents single line of code. Contains
        information about parent

        :param line: code line, String
        """
        self.command = LineParser(line).command
        self.parent = None
        self.command.set_parent(self)


    def write_out(self, sqf=False):
        """Write out

        returns line contents with ; added to the end.

        :return: String
        """
        if sqf:
            line = self.command.write_sqf()
        else:
            line = self.command.write_out()
        if is_pre_block_command(self):
            return self.indent() + line
        else:
            return self.indent() + line + ";\n"
    def __len__(self):
        return len(self.command)

    def __getitem__(self, item):
        return self.command[item]