from elements.compare_elements import *
from elements.math_elements import *
from elements.datatype_elements import *
from elements.code_elements import *

def merge_two_dicts(x: dict, y: dict) -> dict:
    '''Given two dicts, merge them into a new dict as a shallow copy.'''
    z = x.copy()
    z.update(y)
    return z



COMMANDS = {
    "hint": HintElement,
    "random": RandomElement,
    "while": WhileElement,
    "if": IfElement,
    "elif": ElifElement,
}

MATH_COMMANDS = {
    ">": GreaterElement,
    "<": LessElement,
    "=": SetElement,
    "+": PlusElement,
    "-": MinusElement,
    "==": EqualsElement,
    "!=": NotEqualsElement
}

NO_PARAM_COMMANDS = {
    "else": ElseElement,
}

ALL_COMMANDS = merge_two_dicts(COMMANDS, merge_two_dicts(MATH_COMMANDS, NO_PARAM_COMMANDS))

PRE_BLOCK_COMMANDS = (
    IfElement,
    ElifElement,
    ElseElement,
    WhileElement,
)