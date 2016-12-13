from abc import ABCMeta, abstractproperty


class ExtendedList(list, metaclass=ABCMeta):

    @abstractproperty
    def opening_bracket(self):
        return "["

    @abstractproperty
    def closing_bracket(self):
        return "]"

    def __str__(self):
        s = list.__str__(self)
        return self.opening_bracket + s + self.closing_bracket


class CurlyList(ExtendedList):
    opening_bracket = "{"
    closing_bracket = "}"


class RoundList(ExtendedList):
    opening_bracket = "("
    closing_bracket = ")"


if __name__ == "__main__":
    c = CurlyList()
    c.append("asd")
    c.append("kek")
    print(c)
    r = RoundList()
    r.append(1)
    r.append(c)
    print(r)
    print(r[1])
