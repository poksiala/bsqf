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
    "ammo": AmmoElement,
    "primaryWeapon": PrimaryWeaponElement,
    "abs": AbsElement,
    "mod": RemainderElement,
    "ceil": CeilElement,
    "floor": FloorElement,
    "cos": CosElement,
    "acos": AcosElement,
    "sin": SinElement,
    "asin": AsinElement,
    "tan": TanElement,
    "atan": AtanElement,
    "sqrt": SqrtElement,
    "ln": LnElement,
    "exp": ExpElement,
    "deg": DegElement,
    "rad": RadElement,
    "log": LogElement,
    "round": RoundElement,
}


TWO_SIDED_COMMANDS = {
    ">": GreaterElement,
    "<": LessElement,
    "=": SetElement,
    "+": PlusElement,
    "-": MinusElement,
    "==": EqualsElement,
    "!=": NotEqualsElement,
    "%": RemainderElement,
    "^": PowerElement,
    "**": PowerElement,
    "+=": AdditionElement,
    "-=": NegationElement,
}

SET_COMMANDS = {
    "+=": AdditionElement,
    "-=": NegationElement,
    "=": SetElement,
}


NO_PARAM_COMMANDS = {
    "else": ElseElement,
    "player": PlayerElement,
}



ALL_COMMANDS = merge_two_dicts(COMMANDS, merge_two_dicts(TWO_SIDED_COMMANDS, NO_PARAM_COMMANDS))


PRE_BLOCK_COMMANDS = (
    IfElement,
    ElifElement,
    ElseElement,
    WhileElement,
)
