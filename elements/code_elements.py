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

    def write_out(self, sqf=False):
        pass

    def write_sqf(self):
        return self.write_out(sqf=True)

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
    VOID = "Void"

    ANY = "AnyType"
    VARIABLE = "Variable"

    @abstractmethod
    def write_out(self, sqf=False):
        pass

    def write_sqf(self):
        return self.write_out(sqf=True)

    def __str__(self):
        return self.write_out()

    def get_type(self):
        return self.type


class CodeElement(GenericElement, metaclass=ABCMeta):
    pass


class CommandElement(CodeElement, metaclass=ABCMeta):

    def input_warning(self, error: str="input error"):
        print(error)


class SelectElement(CommandElement):

    def __init__(self, array: GenericElement, index: GenericElement):
        self.array = array
        self.index = index

    def write_out(self, sqf=False):
        if sqf:
            return "({} select {})".format(self.array.write_sqf(),
                                           self.index.write_sqf())
        else:
            return "{}[{}]".format(self.array.write_out(),
                                   self.index.write_out())


class VariableElement(GenericElement):

    def __init__(self, name: str):
        self.name = name
        self.type = self.VARIABLE

    def write_out(self, sqf=False):
        return self.name


class SetElement(CommandElement):

    def __init__(self, left: VariableElement, right: GenericElement):
        self.left = left
        self.right = right
        self.type = self.VOID

    def write_out(self, sqf=False):
        return "{} = {}".format(self.left.write_out(sqf),
                                self.right.write_out(sqf))


class ControlElement(CommandElement, metaclass=ABCMeta):
    from elements.block import Block

    def __init__(self, condition: GenericElement, block: Block):
        if condition.type != self.VARIABLE and condition.type != self.BOOL:
            self.input_warning()
        self.condition = condition
        self.block = block


class IfElement(ControlElement):

    def write_out(self, sqf=False):
        return "if ({}) then {}".format(self.condition.write_out(sqf),
                                        self.block.write_out(sqf))


class ElseElement(ControlElement):
    from elements.block import Block

    def __init__(self, block: Block):
        self.block = block

    def write_out(self, sqf=False):
        return "else {}".format(self.block.write_out(sqf))


class ElifElement(ControlElement):

    def write_out(self, sqf=False):
        if sqf:
            return " else { if ({}) then {} }".format(self.condition.write_out(sqf),
                                                      self.block.write_out(sqf))


class WhileElement(ControlElement):

    def write_out(self, sqf=False):
        if sqf:
            return "while { {} } do ".format(self.condition.write_sqf(),
                                             self.block.write_sqf())
        else:
            return "while ( {} ) ".format(self.condition.write_out(),
                                          self.block.write_out())
