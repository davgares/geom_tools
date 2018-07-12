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


def polygon_2_linestring(poly):

    # Transform a shapely.Polygon into a shapely.LineString
    return LineString(list(poly.exterior.coords))


def identify_common_side_polygons(poly1, poly2):

    polylinestring1 = polygon_2_linestring(poly1)
    polylinestring2 = polygon_2_linestring(poly2)

    return polylinestring1.intersection(polylinestring2)


def create_polygon_triangle_side(poly, side_linestring):
    
    if side_linestring.geom_type == 'LineString':
    
        center_poly = poly.representative_point()
        p1 = Point(side_linestring.coords[0])
        p2 = Point(side_linestring.coords[1])
        pointlist = [center_poly, p1, p2, center_poly]
        poly = Polygon([[p.x, p.y] for p in pointlist])
    
    else:
        
        poly = loads('POLYGON EMPTY')
    
    return poly
