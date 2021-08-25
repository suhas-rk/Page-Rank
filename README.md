# PAGE-RANK CALCULATOR

---

## INTRODUCTION

This repository contains code for Page rank calculation by a team consisting of:

Prateek Nayak  
Suhas R  
Vikshit Shetty  
Hrish S

The objective of this project is given a large file containing ‘from_node_id’ and ‘to_node_id’ nodes representing web-graph edges, use hadoop (pseudo distributed mode) to iteratively process the data with map-reduce to calculate page rank for each node in a pseudo distributed mode.

The processing is grouped into two map-reduce stages:

1) Stage 1: Convert input file to adjacency list using map reduce  
   At this stage the mapper reduce functions read the input text file and generate two files representing the adjacency list and initial page ranks
   
2) Stage 2: Iterate Map Reduce functions until convergence of page rank values
   - At this stage the mapper reads input from "adj_list" and "v" and for each node i, it emits key-value pairs
  
   - Reducer groups by key and sums up the values to calculate the new page ranks using the formula:  
    
      PR(N) = 0.15 + 0.85 * ( `Σ` ( PR(Xi)/(number of outgoing links from node Xi) ) )  {where Xi is a node pointing to N}
  
   - The newly calculated page rank is stored in a new file
   
   This process is repeated until the page rank values converge (Convergence of values is checked by check_conv.py).
   
--- 

## INSTRUCTIONS TO RUN

This project requires Hadoop Streaming  

Step 1: Start DFS and YARN 
```bash
start-dfs.sh
start-yarn.sh
```

Step 2: Insert input-file(web-Google.txt) into Hadoop Distributed File System(HDFS)
```bash
hdfs dfs -put web-Google.txt <path of directory>
```

Step 3: Specify path to the following files in "iterate-hadoop.sh"  
        1) Input file  
        2) Output  
        3) Mapper 1 and Reducer 1
        4) Mapper 2 and Reducer 2  
        
Step 4: Run "iterate-hadoop.sh"
```bash
./iterate-hadoop.sh
```
