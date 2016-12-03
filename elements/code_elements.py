from utils.config import *


class CodeSegment:

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

class GenericElement:
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


    def get_type(self):
        return self.type


class CodeElement(GenericElement):

    def __str__(self):
        self.write_out()

class StringElement(GenericElement):

    def __init__(self, string):
        self.string = string

    def return_type(self):
        return

    def SQF(self):
        return '"' + self.string + '"'

    def write_out(self):
        return self.string

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

    def SQF(self):
        return str(self.number)

    def write_out(self):
        return str(self.number)

class SelectElement(CommandElement):

    def __init__(self,array, index):
        self.array = array
        self.index = index

    def write_out(self):
        return "{}[{}]".format(self.array.write_out(),
                               self.index.write_out())

    def SQF(self):
        return "({})".format(self.array.write_out(),
                             self.index.write_out())

class MathElement(CommandElement):

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def SQF(self):
        return "({})".format(self.write_out())

class PlusElement(MathElement):
    def write_out(self):
        return "{} + {}".format(self.a.write_out(),
                                self.b.write_out())

class MinusElement(MathElement):
    def write_out(self):
        return "{} - {}".format(self.a.write_out(),
                                self.b.write_out())

class DivideElement(MathElement):
    def write_out(self):
        return "{} / {}".format(self.a.write_out(),
                                self.b.write_out())

class MultiplyElement(MathElement):
    def write_out(self):
        return "{} * {}".format(self.a.write_out(),
                                self.b.write_out())

class RemainderElement(MathElement):
    def write_out(self):
        return "{} % {}".format(self.a.write_out(),
                                self.b.write_out())