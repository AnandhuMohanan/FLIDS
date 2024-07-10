import flwr as fl
import os
import time

# Make tensorflow log less verbose
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

def weighted_average(metrics):
    total_examples = 0
    federated_metrics = {k: 0 for k in metrics[0][1].keys()}
    for num_examples, m in metrics:
        for k, v in m.items():
            federated_metrics[k] += num_examples * v
        total_examples += num_examples
    return {k: v / total_examples for k, v in federated_metrics.items()}

def get_server_strategy():
    return fl.server.strategy.FedAvg(
            min_fit_clients=3,
            min_evaluate_clients=3,
            min_available_clients=3,
            fit_metrics_aggregation_fn=weighted_average,
            evaluate_metrics_aggregation_fn=weighted_average,
        )
    
if __name__ == "__main__":
    start_time = time.time()

    # Run the server
    history = fl.server.start_server(
        server_address="0.0.0.0:8080",
        strategy=get_server_strategy(),
        config=fl.server.ServerConfig(num_rounds=5),
    )

    # Calculate total time
    end_time = time.time()
    total_time = end_time - start_time

    # Process history or print any final summary
    final_round, acc = history.metrics_distributed["accuracy"][-1]
    print(f"After {final_round} rounds of training the accuracy is {acc:.3%}")

    # Prepare summary output
    summary_output = f"[SUMMARY]\nINFO : Run finished 5 rounds in {total_time:.2f}s\n"
    summary_output += f"INFO : History (loss, distributed):\n{history.metrics_distributed['loss']}\n"
    summary_output += f"INFO : History (metrics, distributed, fit):\n{history.metrics_distributed['fit']}\n"
    summary_output += f"INFO : History (metrics, distributed, evaluate):\n{history.metrics_distributed['evaluate']}\n"
    summary_output += f"After {final_round} rounds of training the accuracy is {acc:.3%}"

    # Directory path
    directory_path = r"D:\Users\HP\Desktop"

    # File name
    filename = "output.txt"

    # Full path to the output file
    output_file = os.path.join(directory_path, filename)

    try:
        # Write summary output to file
        with open(output_file, 'w') as f:
            f.write(summary_output)
        print("Summary output successfully written to file.")
    except Exception as e:
        print("Error occurred while writing summary output to file:", e)
