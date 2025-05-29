import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

# Create a figure for kernel types
fig, ax = plt.subplots(figsize=(14, 10))
fig.suptitle('Types of Kernels and Their Working', fontsize=18, fontweight='bold')

ax.axis('off')
ax.set_title('Diagram: Types of Kernels', fontsize=14)

# Define types of kernels with descriptions
kernel_types = [
    ("Monolithic Kernel", "All OS services (file system, memory, I/O, process mgmt) run in kernel mode. High performance but less modular.\nExample: Linux, UNIX"),
    ("Microkernel", "Only essential services (scheduling, IPC, memory) in kernel mode. Others in user mode. More secure and modular.\nExample: MINIX, QNX"),
    ("Hybrid Kernel", "Mix of monolithic & microkernel: essential services in kernel, others in modules. Combines performance and modularity.\nExample: Windows NT, macOS"),
    ("Nano Kernel", "Minimal kernel that only provides hardware abstraction and scheduling. Used in real-time or embedded systems.\nExample: L4 microkernel variants"),
    ("Exo Kernel", "Application-level resource management. Kernel exposes hardware directly, gives control to applications.\nExample: MIT ExoKernel Project"),
]

# Draw rectangles and text for each kernel type
for i, (k_type, desc) in enumerate(kernel_types):
    y = 0.85 - i * 0.16
    ax.add_patch(mpatches.Rectangle((0.05, y), 0.9, 0.13, edgecolor='black', facecolor='#d1e7dd'))
    ax.text(0.1, y + 0.09, k_type, fontsize=14, fontweight='bold', va='top')
    ax.text(0.1, y + 0.04, desc, fontsize=11, va='top', wrap=True)

plt.tight_layout(rect=[0, 0, 1, 0.93])
plt.savefig('./Types_of_Kernels.png')
plt.show()