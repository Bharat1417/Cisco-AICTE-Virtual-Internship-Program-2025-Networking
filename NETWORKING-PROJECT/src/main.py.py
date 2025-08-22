from config_parser import parse_configs
from topology_builder import build_topology
from network_validator import validate_network
from simulation_engine import simulate, simulate_failure
from report_generator import generate_report

if __name__ == "__main__":
    # Step 1: Parse configs
    devices = parse_configs("configs/")
    print("Parsed devices:", devices)

    # Step 2: Build topology
    G = build_topology(devices)
    print("Topology built with nodes:", G.nodes())

    # Step 3: Validate
    issues = validate_network(G)
    if issues:
        print("Validation Issues:")
        for i in issues:
            print("-", i)
    else:
        print("No validation issues found.")

    # Step 4: Simulate traffic
    print(simulate(G, "PC1", "PC6"))
    print(simulate_failure(G, "R2", "PC1", "PC6"))

    # Step 5: Generate report
    generate_report(G, issues)
    print("Report and topology graph generated in /reports/")
