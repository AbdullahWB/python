from graphviz import Digraph

# Create a new directed graph with left-to-right layout
dot = Digraph(
    name="flowchart",
    graph_attr={"rankdir": "LR"},  # Left-to-right layout
    node_attr={"shape": "box", "style": "filled"},  # Default node style
    format="png"  # Output format
)

# Add nodes for each model with labels and colors
dot.node("BERT", label="BERT (2019)\nUnimodal: Text-only", fillcolor="green")
dot.node("CLIP", label="CLIP (2021)\nText + Images", fillcolor="yellow")
dot.node("DALLE", label="DALL·E (2021)\nText + Image generation", fillcolor="yellow")
dot.node("PALME", label="PaLM-E (2023)\nText + Images + Sensors", fillcolor="orange")

# Add edges with labels to show transitions
dot.edge("BERT", "CLIP", label="Added vision (2021)")
dot.edge("CLIP", "DALLE", label="Added image generation (2021)")
dot.edge("DALLE", "PALME", label="Added sensor data + robotics (2023)")

# Render the graph to a file
dot.render("flowchart", view=False)  # Saves as flowchart.png
print("Flowchart generated as flowchart.png")