# Single-link-Clustering

* The data in simple_graph.txt contains 500 nodes. The first line in the file is the number
of nodes. The format of the data is the following in each line there is [node 1] [node2] [edge_cst]. Therefore,
each line gives information about an edge in the graph. The algorithm in greedy_algorthm.py finds the max spacing of a complete graph given the number of clusters. Using a union_find data structure this has a running time of O(m * logn) where
m is the number of edges in the grpah and n is the number of nodes.
* The data in huge_graph.txt represents a graph with 200000 nodes. Each line of the file represents a node in the
graph using 24 bits in binary. Here the distance between two nodes is the hamming distance between their binary representation. The algorithm in greedy_algorithm2.py finds the number of clusters required to have a max-spacing of 3. 
