from collections import defaultdict, Counter


def readin(file):
    input = []
    with open(file) as f:
        tmp_input = f.read().splitlines()
        for item in tmp_input:
            input.append(item.replace(" ", "").split(','))
        return input




def taxicab_dist(a, b):
    return abs(int(a[0]) - int(b[0])) + abs(int(a[1]) - int(b[1]))

def distances_between_points(input, coord):
    distances = []

    for point in input:
        distance = taxicab_dist(point, coord)
        distances.append((distance, point))
    return distances


def graph_sizer(input):
    x_coords = []
    y_coords = []
    extreme = {}
    for coord in input:
        x_coords.append(int(coord[0]))
        y_coords.append(int(coord[1]))
    x_coords.sort()
    y_coords.sort()
    extreme['x'] = x_coords[0], x_coords[-1]
    extreme['y'] = y_coords[0], y_coords[-1]
    return extreme

"""
def find_infinite(input):
    extreme = graph_sizer(input)
    infinite_points = []
    for point in input:
        if int(point[0]) in extreme['x'] or int(point[1]) in extreme['y']:
            infinite_points.append(point)
    return infinite_points
"""


def find_infinite(input, point):
    extreme = graph_sizer(input)
    if int(point[0]) in extreme['x'] or int(point[1]) in extreme['y']:
        return True
    else:
        return False

"""
def find_finite(input):
    return [point for point in input if point not in find_infinite(input)]
"""

def solver(input):
    single_distance = defaultdict(int)
    infinite_points = []
    extreme = graph_sizer(input)
    #finite_points = find_finite(input)
    for x in range(extreme['x'][1] + 1):
        for y in range(extreme['y'][1] + 1):
            point_in_loop = [x, y]
            distances = sorted(distances_between_points(input, point_in_loop))
            if distances[0][0] != distances[1][0]:
                single_distance[str(distances[0][1])] += 1
                if find_infinite(input, point_in_loop):
                    infinite_points.append(str(distances[0][1]))
    
    ans = [value for key, value in single_distance.items() if key not in infinite_points]
    return max(list(ans))

def solver_part_2(input):
    extreme = graph_sizer(input)
    safe_zone_area = 0
    #finite_points = find_finite(input)
    for x in range(extreme['x'][1] + 1):
        for y in range(extreme['y'][1] + 1):
            point_in_loop = [x, y]
            distances = distances_between_points(input, point_in_loop)
            if sum([x[0] for x in distances]) < 10000:
                safe_zone_area += 1
    return  safe_zone_area
    
            





def main():
    input = readin('inputs/input.txt')
    print(solver(input))
    print(solver_part_2(input))





if __name__ == "__main__":
    main()
