from main import *
from line import Line

FILENAME = "testidata.bsqf"


class Parser:
    def __init__(self):
        file = open(FILENAME, "r")
        self.data = file.readlines()
        for i in range(0, len(self.data)):
            self.data[i] = self.data[i].rstrip()
            t = Line(self.data[i])
            print t
        self.parse()


    def parse(self):
        for line in self.data:
            if line.lstrip()[0:2].lower() == "if":
                a = SQFIf(line.lstrip()[2:].lstrip()[:-1].rstrip())
                a.write_out()


if __name__ == "__main__":
    a = Parser()
    print a.data