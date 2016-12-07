
def recursive_print(data, level=0, indent=4):
    """Recursive list print

    :param data: Multidimensional List
    :param level: Starting indent level, Int
    :param indent: Indent width, Int
    :return: None
    """
    for i in range(0, len(data)):
        if type(data[i]) is not list:
            print(" " * indent * level + str(data[i]))
        else:
            recursive_print(data[i], level + 1)


def flatten(l: list) -> list:
    """Flatten list

    Returns one dimensional version of
    multidimensional list given as a parameter.

    :param l: multidimensional list
    :return: list
    """
    if type(l) is not list:
        return [l]
    a = []
    for i in l:
        if type(i) == list:
            for x in flatten(i):
                a.append(x)
        else:
            a.append(i)
    return a


def merge_two_dicts(x: dict, y: dict) -> dict:
    """Merge two dicts

    Merges two dictionaries together. Becomes obsolete
    in Python version 3.5

    :param x: dict
    :param y: dict
    :return: Merged dict
    """
    z = x.copy()
    z.update(y)
    return z


def merge_multiple_dicts(*args) -> dict:
    merged = dict()
    for d in args:
        merged = merge_two_dicts(merged, d)
    return merged


def is_num(string: str) -> bool:
    try:
        float(string)
        return True
    except:
        return False


def is_variable_like(string: str) -> bool:
    if not string[0].isdigit() and string.replace("_", "").isalnum():
        return True
    else:
        return False
