from elements import Element



class Line(Element):

    def __init__(self, line):
        """Line

        Represents single line of code. Contains
        information about parent

        :param line: code line, String
        """
        self.line = line
        self.parent = None


    def write_out(self):
        """Write out

        returns line contents with ; added to the end.

        :return: String
        """
        return self.indent() + self.line + ";\n"

    def __len__(self):
        return len(self.line)

    def __getitem__(self, item):
        return self.line[item]