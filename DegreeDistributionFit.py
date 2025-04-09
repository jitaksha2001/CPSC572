import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
import powerlaw

# Step 1: Load and build the network
edges_df = pd.read_csv("edges.csv")  # Adjust filename if needed
G = nx.from_pandas_edgelist(edges_df, source='source', target='target')

# Step 2: Extract degree list
degrees = [d for _, d in G.degree()]

# Step 3: Fit a power-law distribution
fit = powerlaw.Fit(degrees)
alpha = fit.power_law.alpha
xmin = fit.power_law.xmin

print(f"Power-law alpha (γ): {alpha:.2f}")
print(f"Xmin (minimum degree where fit starts): {xmin}")

# Step 4: Plot degree distribution and fitted power-law
plt.figure(figsize=(8, 6))
fig = fit.plot_pdf(color='b', marker='o', linewidth=2, label='Empirical')
fit.power_law.plot_pdf(color='r', linestyle='--', ax=fig, label='Power-law fit')

# Labels and legend
plt.xlabel("Degree $k$")
plt.ylabel("P(k)")
plt.title("Degree Distribution with Power-law Fit")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
