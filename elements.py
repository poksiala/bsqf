class Element:

    def set_parent(self, parent):
        self.parent = parent

    def write_out(self):
        pass

    def __str__(self):
        return self.write_out()