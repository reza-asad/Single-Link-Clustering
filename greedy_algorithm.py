# Reza Asad
# March 6th, 2016
######################### Algorithms ########################
from collections import defaultdict

# A greedy algrithm that finds the max-spacing k clusters
# We assume the input graph is complete.
def single_link_clustering(edges_costs, num_nodes, k):
    num_clusters = num_nodes
    nodes = range(1,num_nodes+1)
    nodes_leader_dict = dict(zip(nodes, nodes))
    clusters = union_find(nodes_leader_dict)

    # If the number of nodes is less tan the number of 
    # requested clusters
    if num_clusters <= k:
        print "The number of nodes is smaller than k"
        return None
    i = 0
    while num_clusters != k:
        # Find the leaders for the two nodes involved in the edge
        leader1 = clusters.find(edges_costs[i][0])
        leader2 = clusters.find(edges_costs[i][1])
        # Check if the nodes belong to different clusters
        if leader1 != leader2:
            clusters.fuse(leader1, leader2)
            num_clusters -= 1
        i+=1
    # Now that there the k clusters are found return the max-spacing
    while True:
        leader1 = clusters.find(edges_costs[i][0])
        leader2 = clusters.find(edges_costs[i][1])
        # If the nodes belong to different clusters the cost the max-spacing
        if leader1 != leader2:
            return edges_costs[i][2]
        i += 1

# Union_find data structure 
class union_find():
    def __init__(self, node_to_leader):
        self.node_to_leader = node_to_leader
        cluster_nodes = [[i] for i in node_to_leader.iterkeys()]
        self.leader_to_node = dict(zip(node_to_leader.iterkeys(), cluster_nodes))
    # Finds the leader of a node
    def find(self, node):
        return self.node_to_leader[node]
    # Fuses two nodes with different leaders
    def fuse(self, leader1, leader2):
        def change_leader(c1, leader1, leader2):
            for node in c1:
                self.node_to_leader[node] = leader2
            self.leader_to_node[leader2] += c1
            self.leader_to_node[leader1] = None
        cluster1 = self.leader_to_node[leader1]
        cluster2 = self.leader_to_node[leader2]
        if len(cluster1) < len(cluster2):
            change_leader(cluster1, leader1, leader2)
        else:
            change_leader(cluster2, leader2, leader1)


######################## Main ###############################
# Load the data ino a list of tuples edges_costs
# each tuple contains the connected nodes and the
# edge cost
edges_costs = []
data_file = open('data.txt')
num_nodes = int(next(data_file))
nodes = set()
for line in data_file:
    val = line.split()
    edges_costs.append((int(val[0]), int(val[1]), int(val[2])))

# Sort edges_costs according to edge_cost values
edges_costs = sorted(edges_costs, key=lambda x:x[2])
print single_link_clustering(edges_costs, num_nodes, 4)


