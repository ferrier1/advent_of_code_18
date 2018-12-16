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
        distances[str(combination)] = taxicab_dist(combination[0], combination[1])
    return distances


def graph_sizer(input):
    max_x = 0
    max_y = 0
    for x in input:
        if x[0] == 0 or x[1] == 0:
            return True
        elif x[0] > max_x or x[1] > max_y:
            return True









def main():
    #input = readin('inputs/input.txt')
    input = []
    tmp_input = """1, 1
1, 6
8, 3
3, 4
5, 5
8, 9""".splitlines()
    for item in tmp_input:
        input.append(item.replace(" ", "").split(','))
    #print(distances_between_points(input))
    graph_sizer(input)



if __name__ == "__main__":
    main()
