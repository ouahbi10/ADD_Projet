import csv
from io import StringIO
from math import sqrt

def read_csv(file):
    """Reads numeric data from a CSV file object, ignoring non-numeric values."""
    data = []
    text_stream = StringIO(file.read().decode('utf-8'))  # Decode binary file to text
    reader = csv.reader(text_stream)
    for row in reader:
        try:
            data.append([float(item) for item in row])
        except ValueError:
            continue  # Skip rows with non-numeric values
    return data

def euclidean_distance(point1, point2):
    """Calculate the Euclidean distance between two points."""
    return sqrt(sum((p - q) ** 2 for p, q in zip(point1, point2)))

def average_linkage(cluster1, cluster2, data):
    """Calculate the average linkage distance between two clusters."""
    distances = [euclidean_distance(data[i], data[j]) for i in cluster1 for j in cluster2]
    return sum(distances) / len(distances)

def agglomerative_clustering(data, n_clusters):
    """Perform agglomerative hierarchical clustering."""
    # Initial clusters (each data point in its own cluster)
    clusters = [[i] for i in range(len(data))]
    
    while len(clusters) > n_clusters:
        # Find the two closest clusters based on average linkage
        min_distance = float('inf')
        to_merge = (0, 1)  # Default pair of clusters to merge
        for i in range(len(clusters)):
            for j in range(i + 1, len(clusters)):
                distance = average_linkage(clusters[i], clusters[j], data)
                if distance < min_distance:
                    min_distance = distance
                    to_merge = (i, j)
        
        # Merge the two closest clusters
        clusters[to_merge[0]].extend(clusters[to_merge[1]])
        del clusters[to_merge[1]]
    
    # Convert cluster indices to original data points
    clustered_data = [[data[index] for index in cluster] for cluster in clusters]
    return clustered_data


