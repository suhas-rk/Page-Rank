#!/usr/bin/python3
import sys
import json


def main():
    current_key = None
    out_list = []
    f = open(sys.argv[1], "w")
    for inp in sys.stdin:
        line = inp.strip()
        frm, to = line.split("\t")
        if frm == current_key:
            if to == "-":
                continue
            out_list.append(to)
        else:
            if current_key != None:
                if (len(out_list) > 0):
                    print(current_key, json.dumps(out_list), sep="\t")
                f.write(current_key + ",1\n")
            current_key = frm
            out_list = [to] if to != "-" else []

    if current_key != None:
        if (len(out_list) > 0):
            print(current_key, json.dumps(out_list), sep="\t")
        f.write(current_key + ",1\n")
    f.close()


if __name__ == "__main__":
    main()
