from mininet.net import Mininet
from mininet.topo import Topo
from datetime import datetime
import time
import csv
from utils.collect_metrics import collect_metrics
from utils.save_results import save_results
from topologies1 import HybridHierarchicalTopology, LinearTopology, StarTopology, BusTopology

# Function to ping all hosts manually
def ping_all(net):
    hosts = net.hosts
    for host in hosts:
        for target in hosts:
            if host != target:
                result = host.cmd(f'ping -c 1 {target.IP()}')
                if "1 packets transmitted, 1 received" in result:
                    print(f"Ping from {host.name} to {target.name}: Success")
                else:
                    print(f"Ping from {host.name} to {target.name}: Failed")

# Create each topology

def run_hybrid_hierarchical_topology():
    # Define the network
    net = Mininet(topo=HybridHierarchicalTopology())
    net.start()
    time.sleep(2)  # Wait for the network to settle
    ping_all(net)  # Run ping test to simulate traffic
    metrics = collect_metrics(net)
    save_results(metrics, "hybrid_hierarchical_topology_metrics.csv")
    net.stop()

def run_linear_topology():
    # Define the network
    net = Mininet(topo=LinearTopology())
    net.start()
    time.sleep(2)  # Wait for the network to settle
    ping_all(net)  # Run ping test to simulate traffic
    metrics = collect_metrics(net)
    save_results(metrics, "linear_topology_metrics.csv")
    net.stop()

def run_star_topology():
    # Define the network
    net = Mininet(topo=StarTopology())
    net.start()
    time.sleep(2)  # Wait for the network to settle
    ping_all(net)  # Run ping test to simulate traffic
    metrics = collect_metrics(net)
    save_results(metrics, "star_topology_metrics.csv")
    net.stop()

def run_bus_topology():
    # Define the network
    net = Mininet(topo=BusTopology())
    net.start()
    time.sleep(2)  # Wait for the network to settle
    ping_all(net)  # Run ping test to simulate traffic
    metrics = collect_metrics(net)
    save_results(metrics, "bus_topology_metrics.csv")
    net.stop()

# Run all topologies
def run_all_topologies():
    run_hybrid_hierarchical_topology()
    run_linear_topology()
    run_star_topology()
    run_bus_topology()

if __name__ == "__main__":
    run_all_topologies()