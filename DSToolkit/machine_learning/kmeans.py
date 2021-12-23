########################################################################################################################
# KMEANS tries to find k lables for unlabled data: it is an unsupervised problem
# KMEANS can be implemented using the main function (skeleton of the algorithm) and helper functions will implement it
########################################################################################################################


import random
import sys
from pathlib import Path


#############################################
root_path    = Path(__file__).parents
statistical_ = str( root_path[1] ) + '/statistical/'

sys.path.append( statistical_ )
from distances import *

euclidean = Distances()
#############################################



# This function is an example of the function one may use to get Euclidean distance !
def get_distance(point_1, point_2):
    return ( (point_1[0] - point_2[0])**2 + (point_1[1] - point_2[1])**2 )**0.5


def get_labels(data, centroids):

    labels = []

    for point in data:

        min_dist = float('inf')
        label    = None

        for i, centroid in enumerate(centroids):
            new_dist = euclidean.Euclidean(point, centroid)
            if min_dist > new_dist:
                min_dist = new_dist
                label = i

        labels.append(label)

    return labels


def update_centroids(points, labels, k):

    new_centroids = [[0, 0] for _ in range(k)]
    count         = [0] * k

    for point, label in zip(points, labels):
        new_centroids[label][0] += point[0]
        new_centroids[label][1] += point[1]
        count[label] += 1

    for i, (x, y) in enumerate(new_centroids):
        new_centroids[i] = (x / count[i], y / count[i])

    return new_centroids


def should_stop(old_centroids, centroids, threshold=1e-5):

    total_movement = 0

    for old_point, new_point in zip(old_centroids, centroids):
        total_movement += euclidean.Euclidean(old_point, new_point)

    return total_movement < threshold


def random_sample(low, high):
    return low + (high - low) * random.random()


def initialize_centroids(data, k):

    x_min = y_min = float('inf')
    x_max = y_max = float('-inf')

    for point in data:
        x_min = min(point[0], x_min)
        x_max = max(point[0], x_max)
        y_min = min(point[1], y_min)
        y_max = max(point[1], y_max)

    centroids = []
    for i in range(k):
        centroids.append([random_sample(x_min, x_max),
                          random_sample(y_min, y_max)])

    return centroids


########################################################################################################################
# MAIN FUNCTION...
def kmeans(data, k):

    centroids = initialize_centroids(data, k)
    while True:
        old_centroids = centroids
        labels        = get_labels(data, centroids)
        centroids     = update_centroids(data, labels, k)

        if should_stop(old_centroids, centroids):
            break

    return labels









