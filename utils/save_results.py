import csv

def save_results(metrics, filename):
    """
    Save the collected network metrics into a CSV file.

    Args:
    - metrics (dict): A dictionary containing network metrics.
    - filename (str): The name of the CSV file to save the results.

    Example:
    metrics = {
        "latency": "10ms",
        "bandwidth": "1Gbps",
        "packet_loss": "0%"
    }
    """
    # Open the CSV file in write mode
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        
        # Writing headers (metric names)
        writer.writerow(["Metric", "Value"])
        
        # Writing each metric's name and value as a row in the CSV
        for metric, value in metrics.items():
            writer.writerow([metric, value])

    print(f"Results saved to {filename}")
