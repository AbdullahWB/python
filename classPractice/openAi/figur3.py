import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime

# Data for the timeline
models = [
    ("GPT-Neo", datetime(2022, 2, 1), "1.2B, 3.2B, 20B params; Apache 2.0; EleutherAI"),
    ("BLOOM", datetime(2022, 11, 1), "176B params; 46 languages; OpenRAIL-M v1; BigScience"),
    ("LLaMA", datetime(2023, 2, 1), "7B-65B params; Noncommercial; Meta AI"),
    ("LLaMA 2", datetime(2023, 7, 1), "7B, 13B, 70B params; Commercial use; Meta AI")
]

# Create figure
fig, ax = plt.subplots(figsize=(10, 6))
ax.set_title("Timeline of Open-Source LLMs (2021-2023)")
ax.set_ylabel("Accessibility Trend")

# Plot timeline
dates = [m[1] for m in models]
labels = [m[0] for m in models]
annotations = [m[2] for m in models]

for i, (date, label, anno) in enumerate(zip(dates, labels, annotations)):
    ax.plot(date, i, marker="o", color="blue" if i == 0 else "green" if i > 1 else "yellow")
    ax.text(date, i, label, ha="right", va="center")
    ax.text(date, i + 0.2, anno, ha="left", va="center", fontsize=8)

# Customize axes
ax.set_ylim(-0.5, len(models) + 0.5)
ax.set_xlim(datetime(2021, 1, 1), datetime(2023, 12, 1))
ax.xaxis.set_major_locator(mdates.MonthLocator(interval=6))
ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m"))
plt.xticks(rotation=45)

# Add accessibility trend
ax.plot([datetime(2022, 2, 1), datetime(2023, 7, 1)], [0, 3], "g--", label="Growing Accessibility")
ax.legend()

# Save and show
plt.savefig("llm_timeline.png")
plt.show()