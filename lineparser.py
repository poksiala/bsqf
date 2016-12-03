from utils.commands import COMMANDS

class LineParser:

    def __init__(self, line: str):
        #self.line = self.parse_line(line)
        self.segmented_line = self.divide_into_segments(line)

    def parse_line(self):



        return None

    def divide_into_segments(self, line):
        operators = ["=", "!", "<", ">", "|", "&"]
        segment_list = []
        looking_for = None
        start = -1
        end = False
        for i in range(len(line)):
            if looking_for == "int":
                if not line[i].isdigit():
                    end = i
            if looking_for == "str":
                if not line[i].isalnum():
                    end = i
            if looking_for == "'":
                if line[i] == "'":
                    end = i + 1
            if looking_for == '"':
                if line[i] == '"':
                    end = i + 1
            if looking_for == "operator":
                if not line[i] in operators:
                    end = i
            elif looking_for == "pass":
                end = i

            if end:
                segment = line[start: end]
                segment_list.append(segment)
                end = False
                looking_for = None

            if looking_for is None:
                start = i
                if line[i].isspace():
                    start = -1
                elif line[i].isdigit():
                    looking_for = "int"
                elif line[i].isalpha():
                    looking_for = "str"
                elif line[i] == "'":
                    looking_for = "'"
                elif line[i] == '"':
                    looking_for = '"'
                elif line[i] in operators:
                    looking_for = "operator"
                else:
                    looking_for = "pass"

        if looking_for is not None:
            segment_list.append(line[start:])

        return segment_list



    def find_end_of_string_literal(self, line: str, mark: str):
        return line.index(str)


    def is_command(self, string: str):
        if string in COMMANDS.keys():
            return True
        else:
            return False

    def __str__(self):
        return str(self.segmented_line)


if __name__ == "__main__":
    line1 = 'hint("harh" + "asd")'
    line2 = "lol = random(1, 2)"
    print(LineParser(line1))
    print(LineParser(line2))





