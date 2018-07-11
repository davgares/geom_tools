import numpy as np
from scipy.spatial import  distance

def find_neighbours(pindex, triang):
    # From https://stackoverflow.com/questions/12374781/
    # how-to-find-all-neighbors-of-a-given-point-in-a-delaunay-triangulation-using-sci
    # Answer from user2535797
    neighbours = triang.vertex_neighbor_vertices[1][
                        triang.vertex_neighbor_vertices[0][pindex]:triang.vertex_neighbor_vertices[0][pindex + 1]]
    return neighbours


def characterize_neighbours(pindex, neighbours, points,  method='euclidean'):

    #  Distances between pindex and its neighbours
    distances = distance.cdist(np.array(points[pindex]), points[neighbours], method)
    #  Max distance
    max_distance = np.max(distances)
    #  Index max distance
    index_max_distance = np.argmax(distances, axis=1)
    # Min distance
    min_distance = np.min(distances)
    #  Index max distance
    index_min_distance = np.argmin(distances, axis=1)

    return distances[0], index_max_distance[0], max_distance, index_min_distance[0], min_distance
