import networkx as nx

# Create a graph
G = nx.Graph()

# Add edges (connections)
edges = [("A", "B"), ("A", "C"), ("B", "C"), ("D", "E"), ("E", "F"), ("F", "D")]
G.add_edges_from(edges)

# Find the largest connected component
largest_cc = max(nx.connected_components(G), key=len)

print(largest_cc)


# Create a graph
G = nx.Graph()

# Add edges (connections)
edges = [("A", "B"), ("A", "C"), ("B", "C"), ("D", "E"), ("E", "F"), ("F", "D"), ("A", "D")]
G.add_edges_from(edges)

# Find all maximal cliques (fully connected components)
cliques = list(nx.find_cliques(G))
largest_clique = max(cliques, key=len)
print(largest_clique)


print(cliques)

