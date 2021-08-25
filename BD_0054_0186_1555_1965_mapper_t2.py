#!/usr/bin/python3
import sys
import json


def main():
    f_path = sys.argv[1]
    f = open(f_path, "r")
    node = ""
    for inp in sys.stdin:
        cleand_inp = inp.strip("\n ")
        if len(cleand_inp) == 0:
            continue
        frm, to_list = cleand_inp.split("\t")
        while frm > node:
            fline = f.readline().strip("\n")
            node, rank = fline.split(",")
        rank = float(rank)
        outgoing = json.loads(to_list)
        outgoing_len = len(outgoing)
        print(frm, "[", sep="\t")
        for j in outgoing:
            print(j, rank / outgoing_len, sep="\t")


if __name__ == "__main__":
    main()
