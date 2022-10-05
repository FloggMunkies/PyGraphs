import networkx as nx


class Graph(object):
    def __init__(self):
        self.node_dict = {}
        self.adj_list = {}
        self.edge_dict = {}

    def add_node(self, node):
        if node not in self.node_dict:
            self.node_dict[node.id] = node
        else:
            print("Node ", node, ": ", node.id, " already exists!")

    def add_edge(self, node1, node2, edge, weight, directed=True):
        temp = []
        if node1.id in self.node_dict and node2.id in self.node_dict:
            if node1 not in self.adj_list:
                temp.append([node2, edge, weight])
                self.adj_list[node1] = temp

            elif node1 in self.adj_list:
                temp.extend(self.adj_list[node1])
                temp.append([node2, edge, weight])
                self.adj_list[node1] = temp
            if directed:
                self.print_list_all()
                return
            else:
                temp = []
                if node2 not in self.adj_list:
                    temp.append([node1, edge, weight])
                    self.adj_list[node2] = temp

                elif node2 in self.adj_list:
                    temp.extend(self.adj_list[node2])
                    temp.append([node1, edge, weight])
                    self.adj_list[node2] = temp

        else:
            print("Nodes don't exist!")

    def remove_node(self, node):
        if type(node) is int:
            self.remove_all_edges(self.node_dict[node])
            del self.node_dict[node]
        else:
            key_list = list(self.node_dict.keys())
            val_list = list(self.node_dict.values())
            pos = val_list.index(node)
            id = key_list[pos]
            self.remove_all_edges(node)
            del self.node_dict[id]

    def remove_edge(self, node1, node2):
        pass

    def remove_all_edges(self, node):
        # Loop through each node to see if it points to deleted node
        for n in self.adj_list:
            print("Looking through node:", n.id)
            for i, subedge in enumerate(self.adj_list[n]):
                if subedge[0] == node:
                    print("Node", n.id, "connects to", node.id)
                    subedge[1].delete()
                    del self.adj_list[n][i]
        # del self.adj_list[node]
        if node not in self.adj_list:  # Stop if node has no edges
            print("Total adj list:")
            self.print_list_all()
            return

        # loop through each edge originating
        for edge in self.adj_list[node]:
            edge[1].delete() # Delete the edge widget
            node2 = edge[0]
            print("Node2 ", node2, node2.id)
            if node2 in self.adj_list:
                print(node2.id, " in adj list")
                for i, subedge in enumerate(self.adj_list[node2]):
                    print(i, subedge[0])
                    if subedge[0] == node:
                        print("Doing thing")
                        del self.adj_list[node2][i]

        del self.adj_list[node]
        print("Total adj list:")
        self.print_list_all()

    def test(self):
        pass

    def print_graph(self):
        for node in self.node_dict:
            print(node, ": ", self.node_dict[node])

    def print_list_all(self):
        for node in self.adj_list:
            self.get_list(node, prnt=True)

    def get_list(self, node, prnt=False):
        temp = []
        if node in self.adj_list:
            for edge in self.adj_list[node]:
                temp.append([edge[0].id, edge[2]])
            if prnt:
                print(node.id, ":", temp)
        return temp


graph = Graph()

if __name__ == '__main__':
    pass
    # Adding nodes
    # graph.add_node(0)
    # graph.add_node(1)
    # graph.add_node(2)
    # # Adding edges
    # graph.add_edge(0, 1, 2)
    # graph.add_edge(1, 2, 2)
    #
    # # Printing the graph
    # graph.print_graph()
    #
    # # Printing the adjacency list
    # print(graph.adj_list)
