# Networking Topology Simulation – CISCO VIP 2025

## 📖 Project Overview
This project is developed as part of the **CISCO VIP Networking 2025 Industry Problem Statement**.  
It simulates a network topology using configuration files, validates network settings, and generates reports & visualizations.

The project:
- Reads device configurations (Routers, Switches, PCs) from `configs/`
- Builds a logical topology using **NetworkX**
- Validates the network (duplicate IPs, missing gateways, VLANs, etc.)
- Simulates traffic and node failures
- Generates reports (`report.json`) and a topology graph (`topology.png`)

---

## 📂 Folder Structure
Networking-Project/
│── configs/ # Input device configuration files (R1.txt, S1.txt, PC1.txt, etc.)
│── src/ # Source code
│ ├── config_parser.py
│ ├── topology_builder.py
│ ├── network_validator.py
│ ├── simulation_engine.py
│ ├── report_generator.py
│ ├── main.py
│── reports/ # Generated outputs (report.json, topology.png)
│── requirements.txt
│── README.md

---

## ⚙️ Installation
Make sure you have **Python 3.x** installed.  
Then install the dependencies using:

```bash
pip install -r requirements.txt
▶️ Running the Project
Run the main script:

python src/main.py
📊 Expected Output
Console Output → parsed devices, validation results, simulation paths

reports/report.json → detailed validation report

reports/topology.png → network graph visualization

📌 Example Output
Parsed devices: {'R1': {...}, 'PC1': {...}, ...}
Topology built with nodes: ['R1', 'R2', 'R3', 'S1', 'S2', 'S3', 'PC1', 'PC2', 'PC3', 'PC4', 'PC5', 'PC6']
No validation issues found.
Path from PC1 to PC6: PC1 -> S1 -> R1 -> R2 -> R3 -> S3 -> PC6
Path from PC1 to PC6 after failure of R2: No path found between PC1 and PC6
Report and topology graph generated in /reports/
📑 Reports Generated
Topology Graph → reports/topology.png

Validation Report → reports/report.json


🙌 Author
Bharat P

Submitted as part of CISCO VIP Networking 2025 Problem Statement