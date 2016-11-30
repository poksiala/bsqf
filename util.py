def recursive_print(data, level=0, indent=4):
    """Recursive list print

    :param data: Multidimensional List
    :param level: Starting indent level, Int
    :param indent: Indent width, Int
    :return: None
    """
    from types import StringType
    for i in range(0, len(data)):
        if type(data[i]) == StringType:
            print " " * indent * level + data[i]
        else:
            recursive_print(data[i], level + 1)