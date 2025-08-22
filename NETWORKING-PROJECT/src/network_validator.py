def validate_network(G):
    issues = []

    # Check duplicate IPs
    seen_ips = {}
    for node, data in G.nodes(data=True):
        for intf in data.get("interfaces", []):
            ip = intf["ip"]
            if ip in seen_ips:
                issues.append(f"Duplicate IP {ip} on {node} and {seen_ips[ip]}")
            else:
                seen_ips[ip] = node

    # Check PCs have gateways
    for node, data in G.nodes(data=True):
        if node.startswith("PC"):
            if "gateway" not in data:
                issues.append(f"{node} has no gateway defined.")

    return issues
