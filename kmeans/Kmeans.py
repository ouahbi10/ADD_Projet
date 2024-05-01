import csv
from math import sqrt, fsum
from random import sample
from collections import defaultdict
from functools import partial
from io import StringIO

def read_data_from_csv(file):
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



def mean(data):
    'Accurate arithmetic mean'
    if isinstance(data,list)==False:
        data = list(data)
    return fsum(data) / len(data)

def transpose(matrix):
    'Swap rows with columns for a 2-D array'
    return zip(*matrix)

def distance(p, q, sqrt=sqrt, fsum=fsum, zip=zip):
    'Multi-dimensional euclidean distance between points p and q'
    return sqrt(fsum((x1 - x2) ** 2.0 for x1, x2 in zip(p, q)))

def assign_data(centroids, data):
    """Assign data the closest centroid"""
    d = defaultdict(list)
    for point in data:
        # Convert centroid to a tuple to use it as a dictionary key
        centroid = min(centroids, key=partial(distance, point))
        d[tuple(centroid)].append(point)
    return dict(d)


def compute_centroids(groups):
    """Compute the centroid of each group"""
    return [list(map(mean, transpose(group))) for group in groups]

def k_means(data, k=2, iterations=10):
    """Return k-centroids for the data"""
    data = list(data)
    # Ensure centroids are initialized as tuples if needed
    centroids = [tuple(point) for point in sample(data, k)]
    for i in range(iterations):
        labeled = assign_data(centroids, data)
        # Convert tuples back to lists if necessary
        centroids = [list(centroid) for centroid in compute_centroids(labeled.values())]
    return centroids


def quality(labeled):
    'Mean value of squared distances from data to its assigned centroid'
    return mean(distance(c, p) ** 2 for c, pts in labeled.items() for p in pts)

