import networkx as nx

def generate_and_save_graph(N, p, filename):
    """
    Generate a random undirected graph and save its edge list to a file in Mosel-compatible format.
    
    Args:
        N (int): Number of nodes (e.g., 20, 40, 60)
        p (float): Edge probability (e.g., 0.1, 0.3, 0.5)
        filename (str): Output file name (e.g., "N20_p0.1.txt")
    """
    # Create random graph with fixed seed for reproducibility
    G = nx.erdos_renyi_graph(N, p, seed=42)
    
    # Write to file with space-separated values (Mosel preferred format)
    with open(filename, 'w') as f:
        f.write("EdgeList: [\n")
        for (i, j) in G.edges():
            f.write(f"  [{i+1} {j+1}]\n")  # Space-separated, 1-based indexing
        f.write("]\n")
    
    print(f"Generated graph: {filename} (N={N}, p={p}, edges={G.number_of_edges()})")

# Generate all required graph instances
if __name__ == "__main__":
    # Parameters from your lab description
    node_sizes = [20, 40, 60]
    probabilities = [0.1, 0.3, 0.5]
    
    for N in node_sizes:
        for p in probabilities:
            filename = f"N{N}_p{p}.txt"
            generate_and_save_graph(N, p, filename)
    
    print("\nAll graph files generated successfully.")
