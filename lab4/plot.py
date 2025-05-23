import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Configure plot style - UPDATED
sns.set_theme(style="whitegrid")  # Modern seaborn style
plt.rcParams['figure.dpi'] = 300
plt.rcParams['font.family'] = 'serif'

# Process experimental data
data = {
    'N': [20, 20, 40, 40, 60, 60, 20, 20, 40, 40, 60, 60],
    'p': [0.2, 0.4, 0.2, 0.4, 0.2, 0.4, 0.2, 0.4, 0.2, 0.4, 0.2, 0.4],
    'Edges': [39, 71, 142, 302, 322, 709, 39, 71, 142, 302, 322, 709],
    'd': [1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2],
    'Spectrum': [3, 5, 4, 6, 5, 8, 6, 10, 8, 12, 10, 16],
    'Time': [0.025, 0.029, 0.026, 0.023, 0.017, 0.027, 0.003, 0.029, 0.018, 0.003, 0.026, 0.024]
}
df = pd.DataFrame(data)

# Create plots
fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(18, 5))

# Plot 1: Spectrum vs p
for d in [1, 2]:
    for n in [20, 40, 60]:
        subset = df[(df['d'] == d) & (df['N'] == n)]
        ax1.plot(subset['p'], subset['Spectrum'],
                 marker='o' if d == 1 else 's',
                 linestyle='-' if d == 1 else '--',
                 label=f'N={n},d={d}',
                 markersize=8)
ax1.set_xlabel('Edge Probability (p)', fontsize=12)
ax1.set_ylabel('Spectrum Width', fontsize=12)
ax1.set_title('(a) Spectrum vs. Density', fontsize=13)
ax1.legend()

# Plot 2: Runtime
scatter = ax2.scatter(df['Edges'], df['Time'], c=df['d'], cmap='viridis', s=100)
ax2.set_xlabel('Edge Count', fontsize=12)
ax2.set_ylabel('Runtime (s)', fontsize=12)
ax2.set_title('(b) Computational Complexity', fontsize=13)
cbar = plt.colorbar(scatter, ax=ax2)
cbar.set_label('Spacing (d)', fontsize=12)

# Plot 3: Spacing impact
for n in [20, 40, 60]:
    subset = df[df['N'] == n]
    ax3.plot(subset['d'], subset['Spectrum'], 'o-', label=f'N={n}')
ax3.set_xlabel('Minimum Spacing (d)', fontsize=12)
ax3.set_ylabel('Spectrum Width', fontsize=12)
ax3.set_title('(c) Spacing Impact', fontsize=13)
ax3.legend()

plt.tight_layout()
plt.savefig('freq_allocation.png', dpi=300, bbox_inches='tight')
plt.show()
