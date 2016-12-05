from abc import ABCMeta, abstractmethod
from utils.config import INDENT_WIDTH


class CodeSegment(metaclass=ABCMeta):
    parent = None

    def set_parent(self, parent):
        self.parent = parent

    def get_level(self, level=0):
        if self.parent is not None:
            return self.parent.get_level(level+1)
        else:
            return level

    def indent(self):
        return " " * INDENT_WIDTH * self.get_level()

    @abstractmethod
    def write_out(self, sqf=False):
        pass

    @abstractmethod
    def is_pre_block(self):
        pass

    def write_sqf(self):
        return self.write_out(sqf=True)

    def __str__(self):
        string = self.write_out()
        return str(string)


class Block(CodeSegment):

    def __init__(self):
        """Block

        Block represents single block of source code
        defined with { and }. It has information about
        it's contents and its parent.
        """
        self.parent = None
        self.content = []

    def add_element(self, element):
        """Add element to block

        Appends element given as a parameter
        to the blocks contents. Sets self as a
        parent to the element.

        :param element: Line or Block
        :return: None
        """
        element.set_parent(self)
        self.content.append(element)

    def add_element_list(self, element_list):
        """Add list of elements to block

        Appends elements given as a list to
        the blocks contents. Sets self as a
        parent to all of them

        :param element_list: List[Line, Block]
        :return: None
        """
        for element in element_list:
            self.add_element(element)

    def write_out(self, sqf=False):
        """Write out

        Formats blocks content to string and returns it.
        Curly braces ({}) are added to beginning and to end
        of the string except for the outermost level

        :return: String
        """
        string = ""
        for element in self.content:
            string += element.write_out(sqf)

        if self.get_level() > 0:
            string = self.indent() + "{\n" + string + self.indent() + "}\n"
        return string

    def is_pre_block(self):
        return False

    def __len__(self):
        return len(self.content)

    def __getitem__(self, item):
        return self.content[item]
