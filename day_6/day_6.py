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
        x_coords.append(coord[0])
        y_coords.append(coord[1])
    extreme['x'] = int(sorted(x_coords)[0]), int(sorted(x_coords)[-1])
    extreme['y'] = int(sorted(y_coords)[0]), int(sorted(y_coords)[-1])
    return extreme


def find_infinite(input):
    extreme = graph_sizer(input)
    infinite_points = []
    for point in input:
        if int(point[0]) in extreme['x'] or int(point[1]) in extreme['y']:
            infinite_points.append(point)
    return infinite_points


def find_finite(input):
    return [point for point in input if point not in find_infinite(input)]


def solver(input):
    single_distance = defaultdict(int)
    extreme = graph_sizer(input)
    finite_points = find_finite(input)
    for x in range(0, extreme['x'][1] + 1, 1):
        for y in range(0, extreme['y'][1] + 1, 1):
            point_in_loop = [x, y]
            distances = sorted(distances_between_points(input, point_in_loop))
            if distances[0][0] != distances[1][0] and distances[0][1] in finite_points:
                single_distance[str(distances[0][1])] += 1
    return single_distance




def main():
    input = readin('inputs/input.txt')
    print(solver(input))




if __name__ == "__main__":
    main()
