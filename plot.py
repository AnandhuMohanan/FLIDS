import matplotlib.pyplot as plt
import os

# Loss data
loss_data = {
    1: 1.0768674612045288,
    2: 0.4758925139904022,
    3: 0.4465745687484741,
    4: 0.4131815731525421,
    5: 0.45606303215026855
}

# Metric data
metric_data = {
    'binary_accuracy': [(1, 0.9177184303601583),
                        (2, 0.9312178293863932),
                        (3, 0.9336150685946146),
                        (4, 0.9348013202349345),
                        (5, 0.9353773395220438)],
    'loss': [(1, 0.20411745210488638),
             (2, 0.17187572022279105),
             (3, 0.1600524882475535),
             (4, 0.15115996698538461),
             (5, 0.14681994915008545)]
}

# Extracting metrics for plotting
metric_name = 'binary_accuracy'
rounds, values = zip(*metric_data[metric_name])

# Plotting
plt.figure(figsize=(10, 5))
plt.plot(rounds, values, marker='o', label=metric_name)
plt.plot(loss_data.keys(), loss_data.values(), marker='x', label='Loss')
plt.title('Training Metrics')
plt.xlabel('Round')
plt.ylabel(metric_name.capitalize())
plt.legend()
plt.grid(True)

# Save the plot
save_path = r"D:\Users\HP\Downloads\Test1\fl-ids-main (1)\fl-ids-main\plot.png"
plt.savefig(save_path)

plt.show()
