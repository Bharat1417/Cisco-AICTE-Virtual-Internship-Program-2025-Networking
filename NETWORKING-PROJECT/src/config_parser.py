import os

def parse_configs(config_folder):
    devices = {}

    for filename in os.listdir(config_folder):
        if filename.endswith(".txt"):
            path = os.path.join(config_folder, filename)
            with open(path, "r") as f:
                lines = f.readlines()

            device = {"interfaces": [], "vlans": [], "protocols": []}
            hostname = None

            for line in lines:
                line = line.strip()

                # Hostname
                if line.startswith("hostname"):
                    hostname = line.split()[1]
                    device["hostname"] = hostname

                # Interfaces with IP + mask
                if line.startswith("ip address"):
                    parts = line.split()
                    ip = parts[2]
                    mask = parts[3]
                    device["interfaces"].append({"ip": ip, "mask": mask})

                # Bandwidth
                if line.startswith("bandwidth"):
                    bw = line.split()[1]
                    if device["interfaces"]:
                        device["interfaces"][-1]["bandwidth"] = bw

                # VLANs
                if line.startswith("vlan"):
                    vlan_id = line.split()[1]
                    device["vlans"].append(vlan_id)

                # Routing protocols
                if line.startswith("router"):
                    proto = line.split()[1]
                    device["protocols"].append(proto)

                # Gateway (for PCs)
                if line.startswith("gateway"):
                    gw = line.split()[1]
                    device["gateway"] = gw

            if hostname:
                devices[hostname] = device

    return devices


if __name__ == "__main__":
    configs = parse_configs("../configs/")
    for dev, data in configs.items():
        print(dev, data)
