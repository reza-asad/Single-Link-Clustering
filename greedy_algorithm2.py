# Reza Asad
# April 10th, 2016
######################### Algorithms ########################
from greedy_algorithm import union_find
import itertools as itr
# A greedy algrithm that finds the max number of clusters in
# order to have the max-spacing of 2.
# Note: We assume the input graph is complete.
def find_num_clust(nodes, num_bits, max_spacing):
    def alter(node, j):
        altered_nodes = []
        indices = list(itr.combinations(range(num_bits),j))
        for index in indices:
            list_node = list(node)
            for val in index:
                list_node[val] = list_node[val].replace('0','1')
                list_node[val] = list_node[val].replace('1','0')
            altered = "".join(list_node)
            altered_nodes.append(altered)
        return altered_nodes
    # Convert the binary string to int to save space
    clusters = union_find(dict(zip(map(lambda x: int(x,2),nodes), map(lambda x: int(x,2),nodes))))
    num_clusters = len(nodes)
    for j in range(1,max_spacing):
        for node in nodes:
            altered_nodes = alter(node,j)
            for altered in altered_nodes:
                if altered in nodes:
                    leader1 = clusters.find(int(node,2))
                    leader2 = clusters.find(int(altered,2))
                    if leader1 != leader2:
                        clusters.fuse(leader1, leader2)
                        num_clusters -= 1
    return num_clusters

######################## Main ###############################
# Preprocess the data
data_file = open('huge_graph.txt')
first_row = next(data_file).split()
num_nodes = int(first_row[0])
num_bits = int(first_row[1])
nodes = set()
for line in data_file:
    nodes.add(line.strip().replace(' ', ''))
max_spacing = 3
print find_num_clust(nodes,num_bits,max_spacing)