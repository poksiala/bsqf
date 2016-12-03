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

class CodeElement:

    def __init__(self):
        pass

    def __str__(self):
        self.write_out()

class StringElement:

    def __init__(self, string):
        self.string = string

    def return_type(self):
        return

    def write_out(self):
        return self.string

class CommandElement:

    def __init__(self):
        pass

