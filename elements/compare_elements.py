from elements.code_elements import GenericElement, CommandElement
from abc import abstractproperty

class CompareElement(CommandElement):

    def __init__(self, a: GenericElement, b: GenericElement):
        if a.type != b.type and a.type is not self.VARIABLE \
                and b.type is not self.VARIABLE:
            self.input_warning()

        self.a = a
        self.b = b

        self.type = self.BOOL

    def write_out(self, sqf=False):
        return "({} {} {})".format(self.a.write_out(sqf),
                                   self.sign,
                                   self.b.write_out(sqf))

    @abstractproperty
    def sign(self):
        return "=="


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