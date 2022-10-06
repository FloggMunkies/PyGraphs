import networkx as nx
import widgets
# Create Graph
G = nx.Graph()

print(G)


def create_node(graph, **kwargs):
    return widgets.Node(graph, **kwargs)


create_node(G)


