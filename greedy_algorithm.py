# Reza Asad
# March 6th, 2016
######################### Algorithms ########################
# A greedy algrithm that finds the max-spacing k clusters
def single_link_clustering(edges_costs, num_nodes, k):
    i = 0
    num_clusters = num_nodes
    nodes = range(1,num_nodes+1)
    nodes_leader_dict = dict(zip(nodes, nodes))
    clusters = union_find(nodes_leader_dict)

    # If the number of nodes is less tan the number of 
    # requested clusters
    if num_clusters <= k:
        print "The number of nodes is smaller than k"
    while num_clusters != k:
        node1 = edges_costs[i][0]
        node2 = edges_costs[i][1]
        leader1 = clusters.find(node1)
        leader2 = clusters.find(node2)
        if leader1 != leader2:
            clusters.fuse(leader1, leader2)
            print 'leader to node: ', clusters.leader_to_node
            num_clusters -= 1
        i+=1
    return edges_costs[i]

# Union_find data structure 
class union_find():
    def __init__(self, node_to_leader):
        self.node_to_leader = node_to_leader
        nodes_list = [[i] for i in node_to_leader.iterkeys()]
        self.leader_to_node = dict(zip(node_to_leader.iterkeys(), nodes_list))
    # Finds the leader of a node
    def find(self, node):
        return self.node_to_leader[node]
    # Fuses two nodes with different leaders
    def fuse(self, leader1, leader2):
        def change_leader(c1, leader1, leader2):
            for node in c1:
                self.node_to_leader[node] = leader2
            self.leader_to_node[leader2] += c1
            del self.leader_to_node[leader1]
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
# edges_costs = []
# data_file = open('data.txt')
# num_nodes = int(next(data_file))
# for line in data_file:
#     val = line.split()
#     edges_costs.append((int(val[0]), int(val[1]), int(val[2])))

edges_costs = [(2,5,10),(3,5,10),(1,2,5),(2,3,7),(4,3,5)]
# Sort edges_costs according to edge_cost values
edges_costs = sorted(edges_costs, key=lambda x:x[2])
# print 'edges_costs: ', edges_costs
print single_link_clustering(edges_costs, 5, 3)


