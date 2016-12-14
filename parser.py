from elements.brackets import CurlyList, RoundList


def read_file(path: str) -> str:
    """Read file

    reads the file in path stripping all leading and trailing
    whitespace from every line and returns all it's contents
    in one, single line string.

    It also clears rest of the line after comment marker "//"

    :param path: /path/to/file
    :return: file as a string
    """
    string = ""
    with open(path) as f:
        for l in f.readlines():
            s = l.strip()
            # clear comments
            if "//" in s:
                s = s[:s.index("//")]
            string += s
    return string


def get_hierarchy(string: str) -> list:
    """Get hierarchy

    Parses given string and returns a hierarchic list
    based on normal and curly parentheses found in in it.

    Example:
    >>> get_hierarchy("abc(d{ef})g")
    ['abc', ['d', ['ef']], 'g']

    :param string: string
    :return: list
    """
    hl = []     # hierarchy list
    d = 0       # depth
    ts = ""     # temp string
    for i in range(len(string)):
        c = string[i]
        if d < 0:
            break
        elif c in ("(", "{"):
            if d == 0:
                hl.append(ts)
                ts = ""
                # select correct list extension
                if c == "(":
                    hl.append(RoundList(get_hierarchy(string[i + 1:])))
                else:
                    hl.append(CurlyList(get_hierarchy(string[i + 1:])))
            d += 1
        elif c in (")", "}"):
            d -= 1
        elif d == 0:
            ts += c
        else:
            pass
    if ts:
        hl.append(ts)
    return hl


def recursive_split_lines(l: list) -> list:
    """Split lines

    goes trough multidimensional list and splits strings at ";"
    character. Preserves list types.

    :param l: list
    :return: list
    """
    s = []
    for e in l:
        if type(e) == str:
            s += e.split(";")
        elif isinstance(e, CurlyList):
            s.append(CurlyList(recursive_split_lines(e)))
        elif isinstance(e, RoundList):
            s.append(RoundList(recursive_split_lines(e)))
        else:   # is normal list
            s.append(recursive_split_lines(e))
    return s


def clear_empties(l: list) -> list:
    """Clear empty strings

    recursively clears all empty strings from multidimensional list.
    preserves list types

    :param l: Multidimensional list containing strings
    :return: Multidimensional list containing strings
    """
    # TODO: error handling
    cl = []     # cleared list
    for e in l:
        t = type(e)
        if t == str and len(e) > 0:
                cl.append(e)
        elif isinstance(e, list):
            r = clear_empties(e)
            if len(r) == 0:  # is empty list
                pass
            elif t == CurlyList:
                cl.append(CurlyList(r))
            elif t == RoundList:
                cl.append(RoundList(r))
            else:   # is normal list
                cl.append(r)
        else:   # empty string
            pass
    return cl
