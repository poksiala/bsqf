from elements.code_elements import GenericElement


class StringElement(GenericElement):

    def __init__(self, string: str):
        self.string = self._clean_string(string)
        self.type = self.STR

    def _clean_string(self, string):
        return string.replace('"', '""')

    def write_out(self, sqf=False):
        return '"{}"'.format(self.string)


class ArrayElement(GenericElement):

    def __init__(self):
        self.type = self.ARRAY
        self.contents = []

    def write_out(self, sqf=False):
        array_str = "["
        for element in self.contents:
            array_str += "{}, ".format(element.write_out(sqf))
        array_str = array_str[:-2] + "]"
        return array_str


class NumberElement(GenericElement):

    def __init__(self, number: GenericElement):
        self.number = number
        self.type = self.NUM

    def write_out(self, sqf=False):
        return "".format(self.number)


class BooleanElement(GenericElement):

    def __init__(self, value: bool):
        self.value = value
        self.type = self.BOOL

    def write_out(self, sqf=False):
        if sqf:
            return str(self.value).lower()
        else:
            return str(self.value)