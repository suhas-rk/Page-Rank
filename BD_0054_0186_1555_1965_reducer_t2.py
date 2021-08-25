#!/usr/bin/python3
import sys


def main():
    current_node = None
    current_node_record_count = 0
    rank_unchanged = False
    current_total = 0
    out_list = []
    
    for inp in sys.stdin:
        line = inp.strip()
        node, rank = line.split("\t")
        if node == current_node:
            
            if rank[0] != '[':
                rank = float(rank)
                current_total += rank
                current_node_record_count += 1
            else:
                rank_unchanged = True
                
        else:
            
            if current_node != None and rank_unchanged and current_node_record_count == 0:
                print(current_node, 0.15000, sep=",")
            elif current_node != None:
                #Print newly calculated page rank according to the formula
                print(current_node, round((0.15) + (0.85 * current_total), 5), sep=",")
                
            current_node = node
            
            if rank[0] != "[":
                rank = float(rank)
                current_total = rank
                rank_unchanged = False
                current_node_record_count = 1
            else:
                current_total = 0
                rank_unchanged = True
                current_node_record_count = 0

    if current_node != None and rank_unchanged and current_node_record_count == 0:
        print(current_node, 0.15000, sep=",")
    elif current_node != None:
        print(current_node, round((0.15) + (0.85 * current_total), 5), sep=",")


if __name__ == "__main__":
    main()
