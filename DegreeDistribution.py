import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

# Loading edges
edges_df = pd.read_csv("edges.csv") 
G = nx.from_pandas_edgelist(edges_df, source='source', target='target')

# Degree list
degrees = [d for _, d in G.degree()]

# Step 1: Getting degree frequency
import collections
degree_count = collections.Counter(degrees)

# Step 2: Converting to probability
deg, count = zip(*sorted(degree_count.items()))
prob = [c / sum(count) for c in count]  # Normalize

# Step 3: Plotting dots
plt.figure(figsize=(8, 6))
plt.plot(deg, prob, 'o')  # dots
plt.xlabel("Degree k")
plt.ylabel("P(k)")
plt.title("Degree Distribution (Dot Plot)")
plt.grid(True)
plt.show()
