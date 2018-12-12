from itertools import combinations

def readin(file):
    with open(file) as f:
        input = f.read().splitlines()
        return input


def taxicab_dist(a, b):
    return abs(int(a[0]) - int(b[0])) + abs(int(a[1]) - int(b[1]))


def distances_between_points(input):
    distances = {}
    for combination in combinations(input, 2):
        distances[combination] = taxicab_dist(combination[0].replace(" ", "").split(','), combination[1].replace(" ", "").split(','))
    return distances


def main():
    #input = readin('inputs/input.txt')
    input = """1, 1
1, 6
8, 3
3, 4
5, 5
8, 9""".splitlines()
    print(distances_between_points(input))




if __name__ == "__main__":
    main()
