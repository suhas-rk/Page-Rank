#!/usr/bin/python3
import sys


def main():
    for inp in sys.stdin:
        inp = inp.strip().split('\n')
        for j in inp:
            if len(j) == 0:
                continue
            if "# " in j[0: 2]:
                continue

            j = j.replace(" ", "\t")
            _, to = j.split("\t")
            print(j)
            print(to, "-", sep = "\t")


if __name__ == "__main__":
    main()
