from elements.code_elements import GenericElement


class StringElement(GenericElement):

    def __init__(self, string):
        self.string = string

    def write_out(self, sqf=False):
        return '"{}"'.format(self.string)


class ArrayElement(GenericElement):

    def __init__(self):
        self.type = self.ARRAY
        self.contents = []


class NumberElement(GenericElement):
    def __init__(self, number):
        self.number = number
        self.type = self.NUM

    def write_out(self, sqf=False):
        return "".format(self.number)