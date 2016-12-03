from elements.code_elements import CommandElement, GenericElement
from abc import ABCMeta, abstractproperty


class MathElement(CommandElement, metaclass=ABCMeta):

    def __init__(self, a: GenericElement, b: GenericElement):
        self.a = a
        self.b = b

    @abstractproperty
    def sign(self):
        return ""

    def write_out(self, sqf=False):
        if sqf:
            return "({} {} {})".format(self.a.write_out(sqf=True),
                                       self.sign,
                                       self.b.write_out(sqf=True))
        else:
            return "{} {} {}".format(self.a.write_out(),
                                     self.sign,
                                     self.b.write_out())


class PlusElement(MathElement):
    sign = "+"


class MinusElement(MathElement):
    sign = "-"


class DivideElement(MathElement):
    sign = "/"


class MultiplyElement(MathElement):
    sign = "*"


class RemainderElement(MathElement):
    sign = "%"


class PowerElement(MathElement):
    sign = "^"
