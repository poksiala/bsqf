from elements.code_elements import GenericElement
from elements.return_types import *


class StringElement(GenericElement):
    return_type = STR

    def __init__(self, string: str):
        self.string = self._clean_string(string)

    def _clean_string(self, string):
        return string.replace('"', '""')

    def write_out(self, sqf=False):
        return '"{}"'.format(self.string)


class ArrayElement(GenericElement):
    return_type = ARRAY

    def __init__(self):
        self.contents = []

    def add_element(self, element: GenericElement):
        self.contents.append(element)

    def add_element_list(self, element_list: list):
        for element in element_list:
            self.add_element(element)

    def write_out(self, sqf=False):
        array_str = "["
        for element in self.contents:
            array_str += "{}, ".format(element.write_out(sqf))
        array_str = array_str[:-2] + "]"
        return array_str


class NumberElement(GenericElement):
    return_type = NUM

    def __init__(self, number: GenericElement):
        self.number = number

    def write_out(self, sqf=False):
        return "{}".format(self.number)


class BooleanElement(GenericElement):
    return_type = BOOL

    def __init__(self, value: bool):
        self.value = value

    def write_out(self, sqf=False):
        if sqf:
            return str(self.value).lower()
        else:
            return str(self.value)
