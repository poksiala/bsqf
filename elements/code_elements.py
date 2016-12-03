from abc import ABCMeta, abstractmethod

from utils.config import *


class CodeSegment:
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

    def write_out(self):
        pass

    def __str__(self):
        return self.write_out()


class GenericElement(metaclass=ABCMeta):
    type = None

    # Types from OFP
    STR = "String"
    ARRAY = "Array"
    BOOL = "Boolean"
    GROUP = "Group"
    NUM = "Number"
    OBJ = "Object"
    SIDE = "Side"
    # Types from ARMA
    CODE = "Code"
    CONF = "Config"
    CTRL = "Control"
    DISP = "Display"
    SCRPT = "Script(Handle)"
    STRUCTURED = "Structured Text"
    # Types from ARMA2
    DIARY = "Diary_Record"
    TASK = "Task"
    TEAM_MEMBER = "Team_Member"
    NAMESPACE = "Namespace"
    TRANS = "Trans"
    ORIENT = "Orient"
    TARGET = "Target"
    VECT = "Vector"

    @abstractmethod
    def write_out(self, sqf=False):
        pass

    def write_sqf(self):
        return self.write_out(sqf=True)

    def __str__(self):
        return self.write_out()

    def get_type(self):
        return self.type


class CodeElement(GenericElement):
    pass

class StringElement(GenericElement):

    def __init__(self, string):
        self.string = string

    def write_out(self, sqf=False):
        return '"{}"'.format(self.string)

class CommandElement(CodeElement):
    pass

class ArrayElement(CommandElement):

    def __init__(self):
        self.type = self.ARRAY
        self.contents = []

class NumberElement(GenericElement):
    def __init__(self, number):
        self.number = number
        self.type = self.NUM

    def write_out(self, sqf=False):
        return "".format(self.number)

class SelectElement(CommandElement):

    def __init__(self,array, index):
        self.array = array
        self.index = index

    def write_out(self, sqf=False):
        if sqf:
            return "({} select {})".format(self.array.write_sqf(),
                                           self.index.write_sqf())
        else:
            return "{}[{}]".format(self.array.write_out(),
                               self.index.write_out())
