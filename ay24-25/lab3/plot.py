import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Data processing - corrected structure
data = {
    'N': [20,20,20,20,20,20,40,40,40,40,40,40,60,60,60,60,60,60],
    'p': [0.1,0.2,0.4,0.1,0.2,0.4,0.1,0.2,0.4,0.1,0.2,0.4,0.1,0.2,0.4,0.1,0.2,0.4],
    'Edges': [16,39,71,16,39,71,56,142,302,56,142,302,153,322,709,153,322,709],
    'Type': ['uniform','uniform','uniform','unit','unit','unit',
             'uniform','uniform','uniform','unit','unit','unit',
             'uniform','uniform','uniform','unit','unit','unit'],
    'Weight': [8.58,5.77,4.04,13,9,7,12.60,8.95,5.74,23,15,8,16.95,10.61,6.44,26,18,10],
    'Time': [0.040,0.033,0.045,0.037,0.038,0.004,0.028,0.005,0.023,0.048,0.044,0.064,0.055,0.071,0.104,0.053,0.056,0.154]
}

df = pd.DataFrame(data)

# Corrected normalization calculation
def calculate_normalized_weight(row):
    unit_weight = df[(df['N'] == row['N']) &
                     (df['p'] == row['p']) &
                     (df['Type'] == 'unit')]['Weight'].values[0]
    return row['Weight'] / unit_weight

df['NormWeight'] = df.apply(calculate_normalized_weight, axis=1)

# Plotting
fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(18,5))

# Plot 1: Weight vs p
for n in [20,40,60]:
    for t in ['uniform','unit']:
        subset = df[(df['N']==n) & (df['Type']==t)]
        ax1.plot(subset['p'], subset['Weight'], 'o-' if t=='uniform' else 's--',
                 label=f'N={n},{t}', markersize=8)
ax1.set_xlabel('Edge Probability (p)')
ax1.set_ylabel('Max Weight')
ax1.set_title('(a) Solution Weight vs. Density')
ax1.legend()

# Plot 2: Runtime
for t in ['uniform','unit']:
    subset = df[df['Type']==t]
    ax2.scatter(subset['Edges'], subset['Time'], label=t)
ax2.set_xlabel('Edge Count')
ax2.set_ylabel('Time (s)')
ax2.set_title('(b) Runtime Complexity')
ax2.legend()

# Plot 3: Ratio
for n in [20,40,60]:
    subset = df[(df['N']==n) & (df['Type']=='uniform')]
    ax3.plot(subset['p'], subset['NormWeight'], 'o-', label=f'N={n}')
ax3.set_xlabel('Edge Probability (p)')
ax3.set_ylabel('Weight/UnitWeight')
ax3.set_title('(c) Normalized Weight Ratio')
ax3.legend()

plt.tight_layout()
plt.savefig('mwis_analysis.png', dpi=300, bbox_inches='tight')
plt.show()
