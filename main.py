from utils.config import FILENAME
from parser import Parser

if __name__ == "__main__":
    b = Parser(FILENAME).blocks

    print("#### ORIGINAL")
    with open(FILENAME) as f:
        for l in f.readlines():
            print(l)

    print("\n\n#### BSQF")
    print(b.write_out())

    print("\n\n#### SQF")
    print(b.write_sqf())