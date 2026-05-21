import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.special import lambertw
import seaborn as sns

# Configure plot style
plt.style.use('seaborn-v0_8-paper')
sns.set_palette("husl")
plt.rcParams['figure.dpi'] = 300
plt.rcParams['font.family'] = 'serif'

# Experimental data from your results
data = {
    'N': [20, 20, 20, 40, 40, 40, 60, 60, 60],
    'p': [0.1, 0.3, 0.5, 0.1, 0.3, 0.5, 0.1, 0.3, 0.5],
    'Edges': [16, 54, 98, 56, 223, 385, 153, 510, 884],
    'Clique': [2, 4, 5, 3, 4, 7, 4, 5, 9],
    'Time': [0.027, 0.040, 0.045, 0.046, 0.050, 0.053, 0.050, 0.091, 0.112]
}

df = pd.DataFrame(data)


# Theoretical prediction function (Bollobás 1976)
def theoretical_clique(n, p):
    return 2 * np.log(n) / np.log(1 / p)


# Create figure with two subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

# Plot 1: Clique size vs edge probability
for n in df['N'].unique():
    subset = df[df['N'] == n]
    ax1.plot(subset['p'], subset['Clique'], 'o-', label=f'N={n}',
             markersize=8, linewidth=2)

    # Plot theoretical curves
    p_range = np.linspace(0.05, 0.55, 50)
    theory = theoretical_clique(n, p_range)
    ax1.plot(p_range, theory, '--', alpha=0.5)

ax1.set_xlabel('Edge Probability (p)', fontsize=12)
ax1.set_ylabel('Maximum Clique Size ω(G)', fontsize=12)
ax1.set_title('(a) Clique Size vs. Graph Density', fontsize=13)
ax1.grid(True, alpha=0.3)
ax1.legend(title='Graph Size:')

# Plot 2: Runtime analysis
scatter = ax2.scatter(df['Edges'], df['Time'], c=df['N'], s=100,
                      cmap='viridis', alpha=0.8)
ax2.set_xlabel('Number of Edges (|E|)', fontsize=12)
ax2.set_ylabel('Runtime (seconds)', fontsize=12)
ax2.set_title('(b) Computational Complexity', fontsize=13)
ax2.grid(True, alpha=0.3)

# Add colorbar for graph size
cbar = plt.colorbar(scatter, ax=ax2)
cbar.set_label('Graph Size (N)', fontsize=12)

plt.tight_layout()
plt.savefig('clique_analysis.png', bbox_inches='tight', dpi=300)
plt.show()
