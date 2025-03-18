# Re-import libraries after code environment reset
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

# Set up the figure
fig, axs = plt.subplots(2, 1, figsize=(12, 14))
fig.suptitle('Understanding the Kernel in Operating Systems', fontsize=18, fontweight='bold')

# Diagram 1: What is Kernel?
axs[0].set_title('Diagram 1: What is a Kernel?', fontsize=14)
axs[0].axis('off')

# Layers of the OS system structure
layers = ['User Applications', 'System Call Interface', 'Kernel', 'Hardware (CPU, Memory, I/O Devices)']
colors = ['#e2e3e5', '#d1e7dd', '#cfe2ff', '#f8d7da']

for i, (layer, color) in enumerate(zip(layers, colors)):
    axs[0].add_patch(mpatches.Rectangle((0.2, 0.8 - i*0.15), 0.6, 0.1, edgecolor='black', facecolor=color))
    axs[0].text(0.5, 0.85 - i*0.15, layer, ha='center', va='center', fontsize=12, fontweight='bold')

# Diagram 2: Kernel Working Behind the Scenes
axs[1].set_title('Diagram 2: How Kernel Works Behind the Scenes', fontsize=14)
axs[1].axis('off')

# Drawing components of the kernel
kernel_components = ['Process Management', 'Memory Management', 'File System', 'Device Drivers', 'I/O Management', 'Security & Protection']
for i, comp in enumerate(kernel_components):
    axs[1].add_patch(mpatches.Rectangle((0.1, 0.85 - i*0.12), 0.8, 0.09, edgecolor='black', facecolor='#cfe2ff'))
    axs[1].text(0.5, 0.9 - i*0.12, comp, ha='center', fontsize=11)

# Arrows showing interaction
axs[1].annotate('', xy=(0.5, 0.87), xytext=(0.5, 0.98), arrowprops=dict(facecolor='black', arrowstyle='->'))
axs[1].text(0.5, 0.99, 'User/System Calls', ha='center', fontsize=10)
axs[1].annotate('', xy=(0.5, 0.08), xytext=(0.5, 0.1), arrowprops=dict(facecolor='black', arrowstyle='->'))
axs[1].text(0.5, 0.05, 'Hardware Execution', ha='center', fontsize=10)

plt.tight_layout(rect=[0, 0, 1, 0.95])
plt.savefig('./Kernel_Illustration.png')
plt.show()
