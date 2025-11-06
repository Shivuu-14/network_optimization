import csv
import os
from time import sleep

def ping_latency(host1, host2, count=10):
    """
    Measures the round-trip latency and packet loss between two hosts.
    Returns a tuple (average_latency, jitter, packet_loss).
    """
    result = host1.cmd(f"ping -c {count} {host2.IP()}")
    latency = None
    jitter = None
    packet_loss = None

    # Parse the output to get latency, jitter, and packet loss
    if "avg" in result:
        lines = result.split("\n")
        for line in lines:
            if "avg" in line:
                parts = line.split("/")
                latency = float(parts[4])  # average latency
                jitter = float(parts[5])  # jitter value
                packet_loss = float(lines[-3].split()[5].strip('%'))  # packet loss percentage

    return latency, jitter, packet_loss

def measure_bandwidth(host1, host2, duration=10):
    """
    Measures the bandwidth between two hosts using iperf3.
    Returns bandwidth in Mbps.
    """
    result = host1.cmd(f"iperf3 -c {host2.IP()} -t {duration} -J")
    
    # Parse the result (json output)
    bandwidth = None
    try:
        # Find the "received_bytes" value from the iperf3 result
        import json
        result_json = json.loads(result)
        bandwidth = result_json['end']['sum_received']['bits_per_second'] / 1e6  # Convert to Mbps
    except Exception as e:
        print(f"Error measuring bandwidth: {e}")
    
    return bandwidth if bandwidth else 0

def save_all_metrics_to_csv(metrics, save_path="data_collection/results", filename="all_topologies_metrics.csv"):
    os.makedirs(save_path, exist_ok=True)
    csv_file = os.path.join(save_path, filename)

    # Check if file exists already to avoid rewriting headers
    write_header = not os.path.exists(csv_file)

    with open(csv_file, mode='a', newline='') as file:
        writer = csv.writer(file)
        if write_header:
            writer.writerow(["Topology", "Source", "Destination", "Latency (ms)", "Jitter (ms)", "Packet Loss (%)", "Bandwidth (Mbps)"])
        for row in metrics:
            writer.writerow(row)

    print(f"[INFO] Metrics saved to {csv_file}")

def collect_metrics(network, topologies):
    """
    Collects latency, jitter, packet loss, and bandwidth for each topology
    and saves them into a CSV file.
    """
    metrics = []
    
    for topology_name, topology in topologies.items():
        for host1 in topology.hosts:
            for host2 in topology.hosts:
                if host1 != host2:  # No need to ping itself
                    # Measure latency, jitter, and packet loss
                    latency, jitter, packet_loss = ping_latency(host1, host2)
                    
                    # Measure bandwidth
                    bandwidth = measure_bandwidth(host1, host2)

                    # Collect all the metrics
                    metrics.append(
                        (topology_name, host1.name, host2.name, latency, jitter, packet_loss, bandwidth)
                    )

                    # Optional: Sleep between measurements to avoid overwhelming the network
                    sleep(1)
    
    # Save all collected metrics to CSV
    save_all_metrics_to_csv(metrics)
