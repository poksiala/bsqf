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

