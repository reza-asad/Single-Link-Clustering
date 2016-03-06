# Reza Asad
# Algorithm Class
# March 6th, 2016
######################### Algorithms ########################
# A greedy algrithm that finds the max-spacing k clusters
def single_link_clustering(edges_costs, num_nodes, k):
    i = 0
    num_clusters = num_nodes

    # If the number of nodes is less tan the number of 
    # requested clusters
    if num_clusters <= k:
        print "The number of nodes is smaller than k"
    while num_clusters != k:
        node1 = edge_costs[i][0]
        node2 = edge_costs[i][1]
        leader1 = union_find.find(node1)
        leader2 = union_find.find(node2)
        if leader1 != leader2:
            clusters.fuse(leader1, leader2)
            num_clusters -= 1
        i+=1
    return edges_costs[i]

# Union_find data structure 
class union_find():
    def __init__(self, nodes):
        pass
    def find(self, node):
        pass
    def fuse(self, leader1, leader2):
        pass

######################## Main ###############################
# Load the data ino a list of tuples edges_costs
# each tuple contains the connected nodes and the
# edge cost
edges_costs = []
data_file = open('data.txt')
num_nodes = data_file[0]
next(data_file)
for line in data_file:
    val = line.split()
    edges_costs.append((int(val[0]), int(val[1]), int(val[2])))

# Sort edges_costs according to edge_cost values
edges_costs = sorted(edges_costs, key=lambda x:x[2])
single_link_clustering(edges_costs, num_nodes, 4)


