from elements.code_elements import GenericElement, CommandElement
from abc import abstractproperty
from elements.return_types import *


class CompareElement(CommandElement):

    def __init__(self, a: GenericElement, b: GenericElement):
        if a.return_type != b.return_type and a.return_type is not self.return_type \
                and b.return_type is not self.return_type:
            self.input_warning()

        self.a = a
        self.b = b

    def write_out(self, sqf=False):
        return "({} {} {})".format(self.a.write_out(sqf),
                                   self.sign,
                                   self.b.write_out(sqf))

    @abstractproperty
    def sign(self):
        return "=="

    @property
    def return_type(self):
        return BOOL


class EqualsElement(CompareElement):
    sign = "=="


class NotEqualsElement(CompareElement):
    sign = "!="


class AndElement(CompareElement):
    sign = "&&"


class OrElement(CompareElement):
    sign = "||"


class GreaterElement(CompareElement):
    sign = ">"


class GreaterOrEqualElement(CompareElement):
    sign = ">="


class LessElement(CompareElement):
    sign = "<="


class LessOrEqualElement(CompareElement):
    sign = "<="
