from elements import Element


class Block(Element):

    def __init__(self):
        """Block

        Block represents single block of source code
        defined with { and }. It has information about
        it's contents and its parent.
        """
        self.parent = None
        self.content = []

    def add_element(self, element):
        """Add element to block

        Appends element given as a parameter
        to the blocks contents. Sets self as a
        parent to the element.

        :param element: Line or Block
        :return: None
        """
        element.set_parent(self)
        self.content.append(element)

    def add_element_list(self, element_list):
        """Add list of elements to block

        Appends elements given as a list to
        the blocks contents. Sets self as a
        parent to all of them

        :param element_list: List[Line, Block]
        :return: None
        """
        for element in element_list:
            self.add_element(element)

    def write_out(self):
        """Write out

        Formats blocks content to string and returns it.
        Curly braces ({}) are added to beginning and to end
        of the string

        :return: String
        """
        str = ""
        for element in self.content:
            str += element.write_out()

        if self.get_level() > 0:
            str = self.indent() + "{\n" + str +self.indent() + "}\n"
        return str

    def __len__(self):
        return len(self.content)

    def __getitem__(self, item):
        return self.content[item]


