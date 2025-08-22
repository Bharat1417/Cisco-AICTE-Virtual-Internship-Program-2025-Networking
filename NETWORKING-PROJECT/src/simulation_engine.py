import networkx as nx

def simulate(G, src, dst):
    try:
        path = nx.shortest_path(G, src, dst)
        return f"Path from {src} to {dst}: {' -> '.join(path)}"
    except nx.NetworkXNoPath:
        return f"No path found between {src} and {dst}"

def simulate_failure(G, failed_node, src, dst):
    G_removed = G.copy()
    if failed_node in G_removed:
        G_removed.remove_node(failed_node)
    return simulate(G_removed, src, dst)
