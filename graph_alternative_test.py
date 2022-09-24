import networkx as nx

# Create Graph
G = nx.Graph()

# Add Nodes
G.add_node(1)
G.add_nodes_from([2, 3])
G.add_nodes_from([
    (4, {"color": "red"}),
    (5, {"color": "green"}),
])

# H = nx.path_graph(10)
# G.add_nodes_from(H)

# Add Graph as a node
# G.add_node(H)

# Add Edges

G.add_edge(1, 2)
e = (2, 3)
G.add_edge(*e)  # unpack edge tuple*

G.add_edges_from([(1, 2), (1, 3)])

G.clear()
# Create nodes and edges simultaneously
G.add_edges_from([(1, 2), (1, 3)])
G.add_node(1)
G.add_edge(1, 2)
G.add_node("spam")        # adds node "spam"
G.add_nodes_from("spam")  # adds 4 nodes: 's', 'p', 'a', 'm'
G.add_edge(3, 'm')


# Graph has 4 attributes: nodes, edges, adj and degree
print(list(G.nodes))
print(list(G.edges))
print(list(G.adj[1]))  # Neighbors of node 1
print(G.degree[1])  # Number of edges incident to 1

# nbunch
print(G.edges([2, "m"]))


