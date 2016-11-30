class SQFWhile:
    def __init__(self, condition):
        self.condition = condition
        self.lines = []

    def add_line(self, line):
        self.lines.append(line)

    def write_out(self):
        print("while {{{}}} do {{".format(self.condition))


class SQFIf:
    def __init__(self, condition):
        self.condition = condition

    def write_out(self):
        print("if ({}) {{".format(self.condition))



