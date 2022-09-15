
class Graph(object):
    def __init__(self):
        self.node_list = []
        self.adj_list = {}

    def add_node(self, node):
        if node not in self.node_list:
            self.node_list.append(node)
        else:
            print("Node ", node, " already exists!")

    def add_edge(self, node1, node2, weight):
        temp = []
        if node1 in self.node_list and node2 in self.node_list:
            if node1 not in self.adj_list:
                temp.append([node2, weight])
                self.adj_list[node1] = temp

            elif node1 in self.adj_list:
                temp.extend(self.adj_list[node1])
                temp.append([node2, weight])
                self.adj_list[node1] = temp

        else:
            print("Nodes don't exist!")

    def print_graph(self):
        for node in self.adj_list:
            print(node, " ---> ", [i for i in self.adj_list[node]])


graph = Graph()

# # Adding nodes
# graph.add_node(0)
# graph.add_node(1)
# graph.add_node(2)
# # Adding edges
# graph.add_edge(0, 1, 2)
# graph.add_edge(1, 2, 2)
#
#
# # Printing the graph
# graph.print_graph()
#
# # Printing the adjacency list
# print(graph.adj_list)
