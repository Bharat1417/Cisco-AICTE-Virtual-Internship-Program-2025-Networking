import json
import matplotlib.pyplot as plt
import networkx as nx

def generate_report(G, issues, filename="reports/report.json"):
    report = {
        "nodes": list(G.nodes(data=True)),
        "edges": list(G.edges()),
        "validation_issues": issues
    }

    # Save JSON
    with open(filename, "w") as f:
        json.dump(report, f, indent=4)

    # Save topology graph
    plt.figure(figsize=(8, 6))
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_color="lightblue", node_size=1500, font_size=10)
    plt.savefig("reports/topology.png")
    plt.close()
