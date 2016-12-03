from elements.code_elements import CommandElement, GenericElement


class MathElement(CommandElement):

    def __init__(self, a: GenericElement, b: GenericElement):
        self.a = a
        self.b = b


class PlusElement(MathElement):

    def write_out(self, sqf=False):
        if sqf:
            return "({} + {})".format(self.a.write_out(sqf=True),
                                      self.b.write_out(sqf=True))
        else:
            return "{} + {}".format(self.a.write_out(),
                                self.b.write_out())


class MinusElement(MathElement):
    def write_out(self, sqf=False):
        if sqf:
            return "({} - {})".format(self.a.write_out(sqf=True),
                                      self.b.write_out(sqf=True))
        else:
            return "{} - {}".format(self.a.write_out(),
                                    self.b.write_out())


class DivideElement(MathElement):
    def write_out(self, sqf=False):
        if sqf:
            return "({} / {})".format(self.a.write_out(sqf=True),
                                      self.b.write_out(sqf=True))
        else:
            return "{} / {}".format(self.a.write_out(),
                                    self.b.write_out())


class MultiplyElement(MathElement):
        def write_out(self, sqf=False):
            if sqf:
                return "({} * {})".format(self.a.write_out(sqf=True),
                                          self.b.write_out(sqf=True))
            else:
                return "{} * {}".format(self.a.write_out(),
                                        self.b.write_out())


class RemainderElement(MathElement):
    def write_out(self, sqf=False):
        if sqf:
            return "({} % {})".format(self.a.write_out(sqf=True),
                                      self.b.write_out(sqf=True))
        else:
            return "{} % {}".format(self.a.write_out(),
                                    self.b.write_out())

