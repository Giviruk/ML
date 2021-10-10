import matplotlib.pyplot as plt
import numpy as np


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def get_dist(p1, p2):
    return np.sqrt((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2)


def get_random_points(n):
    points = []
    for i in range(n):
        points.append(Point(np.random.randint(0, 100), np.random.randint(0, 100)))
    return points


def get_starting_centroids(points, k):
    x = np.mean(list(map(lambda point: point.x, points)))
    y = np.mean(list(map(lambda point: point.y, points)))
    R = 0
    for p in points:
        R = max(R, get_dist(p, Point(x, y)))

    centroids = []
    for i in range(k):
        centroids.append(Point(x + R * np.cos(2 * np.pi * i / k),
                               y + R * np.sin(2 * np.pi * i / k)))
    return centroids


def get_nearest_centroid(point, centroids):
    list_dists = list(map(lambda centroid: get_dist(point, centroid), centroids))
    my_min_index = list_dists.index(min(list_dists))

    return my_min_index


def get_new_centroid(points):
    x = np.mean(list(map(lambda point: point.x, points)))
    y = np.mean(list(map(lambda point: point.y, points)))
    return Point(x, y)


def get_euclid_dist_square(clusters, centroids):
    dist = 0
    for cluster_index in range(len(clusters)):
        for point in clusters[cluster_index]:
            dist += get_dist(point, centroids[cluster_index]) ** 2
    return dist


def clustering(centroids, is_show_result):
    clusters = []
    for i in range(iteration_count):
        clusters = []
        for ik in range(k):
            clusters.append([])

        for point in points:
            centroid = get_nearest_centroid(point, centroids)
            clusters[centroid].append(point)

        centroids = []
        for ik in range(k):
            centroids.append((get_new_centroid(clusters[ik])))

        if is_show_result:
            show_results(clusters, centroids)

    return clusters, centroids


def show_results(clusters, centroids):
    colors = ['magenta', 'blue', 'green', 'cyan', 'red', 'gold', 'peru', 'purple', 'orange', 'pink']
    for cluster in clusters:
        plt.scatter(list(map(lambda point: point.x, cluster)),
                    list(map(lambda point: point.y, cluster)),
                    color=colors[clusters.index(cluster)])

    plt.scatter(list(map(lambda point: point.x, centroids)),
                list(map(lambda point: point.y, centroids)),
                color='black')
    plt.show()


def get_optimal(distances, points, k):
    dists = []
    for index in range(len(distances) - 1):
        dists.append(abs(distances[index] - distances[index + 1])
                     / abs(distances[index - 1] - distances[index]))

    optimal_index = dists.index(min(dists))

    k = optimal_index + 1
    optimal_centroids = get_starting_centroids(points, k)

    plt.scatter(list(map(lambda point: point.x, points)),
                list(map(lambda point: point.y, points)))

    plt.scatter(list(map(lambda point: point.x, optimal_centroids)),
                list(map(lambda point: point.y, optimal_centroids)),
                color='b')
    plt.show()

    clustering(optimal_centroids, 1)


if __name__ == "__main__":
    point_count = 2000  # кол-во тчк
    iteration_count = 4
    cluster_count = 13  # кол-во кластеров

distances = []
clustering_results = []
centroid_result = []

points = get_random_points(point_count)


for k in range(1, cluster_count):
    centroids = get_starting_centroids(points, k)

    clusters, centroids = clustering(centroids, 0)

    clustering_results.append(clusters)
    centroid_result.append(centroids)
    distances.append(get_euclid_dist_square(clusters, centroids))

get_optimal(distances, points, k)
