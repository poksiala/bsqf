from utils.config import FILENAME
from parser import read_file, get_hierarchy
from utils.util import recursive_print

if __name__ == "__main__":
    print("#### ORIGINAL")
    with open(FILENAME) as f:
        for l in f.readlines():
            print(l)

    s = read_file(FILENAME)
    print(s)

    h = get_hierarchy(s)
    recursive_print(h)
    print(h)