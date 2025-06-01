import os
import json
import matplotlib.pyplot as plt

def load_data(env_dir):
    curves = {}
    for fname in os.listdir(env_dir):
        if fname.endswith(".jsonl"):
            label = fname.replace(".jsonl", "")
            path = os.path.join(env_dir, fname)
            with open(path, "r") as f:
                lines = [json.loads(line) for line in f]
            steps = [entry["step"] for entry in lines]
            returns = [entry["return"] for entry in lines]
            curves[label] = (steps, returns)
    return curves

env = "cartpole"
results = load_data(f"results/{env}")

plt.figure(figsize=(10, 6))
for label, (steps, returns) in results.items():
    plt.plot(steps, returns, label=label)
plt.title(f"Actor-Critic Baselines on {env}")
plt.xlabel("Training Steps")
plt.ylabel("Average Return")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("cartpole_baselines.png")
print("Plot gespeichert als 'lunarlander_baselines.png'")
