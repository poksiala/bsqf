from abc import ABCMeta, abstractmethod, abstractproperty
from elements.return_types import *


class GenericElement(metaclass=ABCMeta):

    parent = None

    @abstractproperty
    def return_type(self):
        return ANY

    @abstractmethod
    def write_out(self, sqf=False) -> str:
        pass

    def set_parent(self, parent):
        self.parent = parent

    def write_sqf(self):
        return self.write_out(sqf=True)

    def __str__(self) -> str:
        return self.write_out()

    def get_type(self):
        return self.return_type


class CommandElement(GenericElement, metaclass=ABCMeta):

    def input_warning(self, error: str="input error"):
        print(error)


class VariableElement(GenericElement):

    return_type = VARIABLE

    def __init__(self, name: str):
        self.name = name

    def write_out(self, sqf=False) -> str:
        return self.name


class SetElement(CommandElement):
    return_type = VOID

    def __init__(self, left: VariableElement, right: GenericElement):
        self.left = left
        self.right = right

    def write_out(self, sqf=False):
        return "{} = {}".format(self.left.write_out(sqf),
                                self.right.write_out(sqf))

class AdditionElement(SetElement):
    return_type = VOID

    def write_out(self, sqf=False):
        if sqf:
            return "{} = {} + {}".format(self.left.write_sqf(),
                                         self.left.write_sqf(),
                                         self.right.write_sqf())
        else:
            return "{} += {}".format(self.left.write_out(),
                                     self.right.write_out())


class NegationElement(SetElement):
    return_type = VOID

    def write_out(self, sqf=False):
        if sqf:
            return "{} = {} - {}".format(self.left.write_sqf(),
                                         self.left.write_sqf(),
                                         self.right.write_sqf())
        else:
            return "{} -= {}".format(self.left.write_out(),
                                     self.right.write_out())




class ControlElement(CommandElement, metaclass=ABCMeta):

    @property
    def return_type(self):
        return VOID

    def __init__(self, condition: GenericElement):
        if condition.return_type != VARIABLE and condition.return_type != BOOL:
            self.input_warning()
        self.condition = condition
        self.block = None

    def set_block(self, block):
        self.block = block
        self.block.set_parent(self.parent)


class IfElement(ControlElement):

    def write_out(self, sqf=False):
        if sqf:
            return "if ({}) then\n {} ".format(self.condition.write_sqf(),
                                               self.block.write_sqf())
        else:
            return "if ({})\n {}".format(self.condition.write_out(),
                                         self.block.write_out())


class ElseElement(ControlElement):

    def __init__(self):
        self.block = None

    def write_out(self, sqf=False):
        return "else\n {} ".format(self.block.write_out(sqf))


class ElifElement(ControlElement):

    def write_out(self, sqf=False):
        if sqf:
            return " else {{ if ({}) then\n {} }}".format(self.condition.write_sqf(),
                                                          self.block.write_sqf())
        else:
            return "elif ({})\n {} ".format(self.condition.write_out(),
                                            self.block.write_out())


class WhileElement(ControlElement):

    def write_out(self, sqf=False):
        if sqf:
            return "while { {} } do ".format(self.condition.write_sqf(),
                                             self.block.write_sqf())
        else:
            return "while ( {} ) ".format(self.condition.write_out(),
                                          self.block.write_out())


class ForEachElement(ControlElement):
    # TODO: doen't output semicolons correctly
    def write_out(self, sqf=False):
        if sqf:
            return "{} forEach {}".format(self.block.write_sqf(),
                                          self.condition.write_sqf())
        else:
            return "{}.forEach({})".format(self.condition.write_out(),
                                           self.block.write_out())


class HintElement(CommandElement):
    return_type = VOID

    def __init__(self, param: GenericElement):
        if param.return_type != STR and param.return_type != VARIABLE:
            self.input_warning()
        self.param = param

    def write_out(self, sqf=False):
        if sqf:
            return "hint {}".format(self.param.write_sqf())
        else:
            return "hint({})".format(self.param.write_out())


class RandomElement(CommandElement):

    return_type = NUM

    def __init__(self, param1: GenericElement, param2: GenericElement):
        if param1.return_type != NUM and param1.return_type != VARIABLE:
            self.input_warning()
        if param2.return_type != NUM and param2.return_type != VARIABLE:
            self.input_warning()
        self.param1 = param1
        self.param2 = param2

    def write_out(self, sqf=False):
        if sqf:
            return "({} + floor random ({} - {}))".format(self.param1.write_sqf(),
                                                          self.param2.write_sqf(),
                                                          self.param1.write_sqf())
        else:
            return "random({},{})".format(self.param1.write_out(),
                                          self.param2.write_out())


class NoParamElement(CommandElement, metaclass=ABCMeta):

    @abstractproperty
    def name(self):
        return "methodName"

    def write_out(self, sqf=False):
        return " {} ".format(self.name)


class PlayerElement(NoParamElement):
    return_type = OBJ
    name = "Player"


class AmmoElement(CommandElement):
    return_type = NUM

    def __init__(self, unit: GenericElement, weapon: GenericElement):
        if unit.return_type is not OBJ and unit.return_type is not VARIABLE:
            self.input_warning()
        if weapon.return_type is not STR and weapon.return_type is not VARIABLE:
            self.input_warning()
        self.a = unit
        self.b = weapon

    def write_out(self, sqf=False):
        if sqf:
            return " {} ammo {} ".format(self.a.write_sqf(), self.b.write_sqf())
        else:
            return "ammo({}, {})".format(self.a.write_out(), self.b.write_out())


class SingleParameterElement(CommandElement, metaclass=ABCMeta):

    def __init__(self, param1: GenericElement):
        if param1.return_type is not VARIABLE and param1.return_type not in self.allowed_types:
            self.input_warning()
        self.param = param1

    @abstractproperty
    def allowed_types(self):
        return [VARIABLE]

    @abstractproperty
    def name(self):
        return "command"

    def write_out(self, sqf=False):
        if sqf:
            return " {} {} ".format(self.name, self.param.write_sqf())
        else:
            return "{}({})".format(self.name, self.param.write_out())


class PrimaryWeaponElement(SingleParameterElement):
    name = "primaryWeapon"
    return_type = STR
    allowed_types = [OBJ]


class ActionNameElement(SingleParameterElement):
    name = "actionName"
    return_type = STR
    allowed_types = [STR]


class IsPlayerElement(SingleParameterElement):
    name = "isPlayer"
    return_type = BOOL
    allowed_types = [OBJ]


class NumToNumElement(SingleParameterElement, metaclass=ABCMeta):
    @property
    def return_type(self):
        return NUM

    @property
    def allowed_types(self):
        return [NUM]


class CeilElement(NumToNumElement):
    name = "ceil"


class FloorElement(NumToNumElement):
    name = "floor"


class AbsElement(NumToNumElement):
    name = "abs"


class AcosElement(NumToNumElement):
    name = "acos"


class CosElement(NumToNumElement):
    name = "cos"


class SinElement(NumToNumElement):
    name = "sin"


class AsinElement(NumToNumElement):
    name = "asin"


class TanElement(NumToNumElement):
    name = "tan"


class AtanElement(NumToNumElement):
    name = "atan"


class SqrtElement(NumToNumElement):
    name = "sqrt"


class LnElement(NumToNumElement):
    name = "ln"


class ExpElement(NumToNumElement):
    name = "exp"


class DegElement(NumToNumElement):
    name = "deg"


class RadElement(NumToNumElement):
    name = "rad"


class LogElement(NumToNumElement):
    name = "log"


class RoundElement(NumToNumElement):
    name = "round"

class SelectElement(CommandElement):
    return_type = ANY

    def __init__(self, array: GenericElement, index: GenericElement):
        self.array = array
        self.index = index

    def write_out(self, sqf=False):
        if sqf:
            return "{} select {} ".format(self.array.write_sqf(),
                                          self.index.write_sqf())
        else:
            return "{}.select({})".format(self.array.write_out(),
                                          self.index.write_out())
