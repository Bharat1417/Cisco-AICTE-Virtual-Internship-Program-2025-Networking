import networkx as nx

def build_topology(devices):
    G = nx.Graph()

    # Add devices as nodes
    for dev, info in devices.items():
        G.add_node(dev, **info)

    # Simple rule: connect routers sequentially and attach PCs/Switches
    routers = [d for d in devices if d.startswith("R")]
    switches = [d for d in devices if d.startswith("S")]
    pcs = [d for d in devices if d.startswith("PC")]

    # Connect routers in a chain
    for i in range(len(routers) - 1):
        G.add_edge(routers[i], routers[i+1])

    # Connect each switch to one router
    for i, sw in enumerate(switches):
        G.add_edge(sw, routers[i % len(routers)])

    # Connect PCs evenly to switches
    for i, pc in enumerate(pcs):
        G.add_edge(pc, switches[i % len(switches)])

    return G

if __name__ == "__main__":
    from config_parser import parse_configs
    devices = parse_configs("../configs/")
    topo = build_topology(devices)
    print("Nodes:", topo.nodes(data=True))
    print("Edges:", topo.edges())
