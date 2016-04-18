# Reza Asad
# April 10th, 2016
######################### Algorithms ########################
from greedy_algorithm import union_find
# A greedy algrithm that finds the max number of clusters in
# order to have the max-spacing of 2.
# Note: We assume the input graph is complete.
def find_num_clust(nodes, num_bits, max_spacing):
    def altered(node, i, j):
        pass
    clusters = 
    num_clusters = len(nodes)
    for j in range(1,max_spacing):
        for node in nodes:
            for i in range(num_bits):
                altered = alter(node,i, j)
                if altered in nodes:
                    leader1 = clusters.find(node)
                    leader2 = clusters.find(altered)
                    if leader != leader:
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
    nodes.add(line)
max_spacing = 3
print find_num_clust(nodes,num_bits,max_spacing)