import matplotlib.pyplot as plt

# Data
models = ["BERT", "GPT-2", "GPT-3", "PaLM"]
energy_mwh = [0.8, 1000, 1287, 9360]  # Energy usage in MWh
colors = ["blue", "green", "orange", "red"]

# Create bar graph
plt.figure(figsize=(8, 6))
bars = plt.bar(models, energy_mwh, color=colors)

# Logarithmic scale for Y-axis
plt.yscale("log")
plt.ylabel("Energy Usage (MWh, Log Scale)")
plt.xlabel("Large Language Models")
plt.title("Energy Usage During Training of LLMs (in MWh)")

# Add annotations
for bar, energy in zip(bars, energy_mwh):
    plt.text(bar.get_x() + bar.get_width() / 2, energy, f"{energy} MWh", 
             ha="center", va="bottom", fontsize=10)

# Adjust layout and save
plt.tight_layout()
plt.savefig("energy_usage_llms.png")
plt.show()