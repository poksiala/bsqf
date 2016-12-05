from elements.code_elements import *
from elements.compare_elements import *
from elements.math_elements import *
from utils.util import merge_two_dicts


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
