# SARS Co-Authorship Network Analysis

This project explores the collaborative structure of SARS-related scientific research prior to the COVID-19 pandemic by constructing and analyzing a co-authorship network.

# Project Structure:
File and Description: 
SARS DATASET - Sheet1.csv: Raw dataset containing SARS-related publications metadata (filtered from CORD-19).
EdgesAndNodes.ipynb: Notebook used to clean the data, extract author information, and generate `edges` and `nodes` CSVs.
Edges File 572.csv: Processed edge list: each row represents a co-authorship pair and its weight.
DegreeDistribution.py: Script to compute and visualize the empirical degree distribution.
DegreeDistributionFit.py: Script to fit and compare the degree distribution to a power-law on a log-log scale.
NullModel_Comparison_SARS_ipynb.ipynb: Jupyter Notebook to create and compare a configuration-based null model against the real network.

# Project Goals:
- Identify **key authors** (high centrality) driving collaboration.
- Detect **communities** using modularity to find closely collaborating subgroups.
- Measure **network density** and structure to understand overall collaboration intensity.
- Compare against a **null model** to test statistical significance of observed structure.

# Tools & Libraries:
- **Python**: For data processing and metric calculation
- `pandas`, `networkx`, `matplotlib`, `collections`
- **Gephi**: For advanced network visualization and modularity/community detection

# Key Findings: 
- ~1,500 unique authors, ~11,000 co-authorship links
- High clustering coefficient: 0.943
- Moderate average path length: ~5
- 135 detected communities using Louvain algorithm
- Null model confirms observed network is **not random** — real-world structure is meaningful

# Output Files: 
- Edges File 572.csv: Final edge list used for graph construction
- Visualizations and analysis results are embedded in the notebooks

# Citation & Dataset Source
- CORD-19 dataset by the Allen Institute for AI:  
  https://www.kaggle.com/datasets/allen-institute-for-ai/CORD-19-research-challenge
  https://github.com/allenai/cord19?tab=readme-ov-file


