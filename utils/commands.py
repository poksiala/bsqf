from elements.compare_elements import *
from elements.math_elements import *
from elements.datatype_elements import *
from elements.code_elements import *

COMMANDS = {
    "hint": HintElement,
    "random": RandomElement,
    "while": WhileElement,
    "if": IfElement,
    "elif": ElifElement,
    "else": ElseElement,
}
MATH_COMMANDS = {
    ">": GreaterElement,
    "<": LessElement,
    "=": SetElement,
    "+": PlusElement,
    "-": MinusElement
}