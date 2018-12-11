from itertools import combinations

def readin(file):
    with open(file) as f:
        input = f.read().splitlines()
        return input


def taxicab_dist(a, b):
    return abs(int(a[0]) - int(b[0])) + abs(int(a[1]) - int(b[1]))


def distances_between_points(input):
    for combination in combinations(input, 2):
        




def main():
    #input = readin('inputs/input.txt')
    input = """1, 1
1, 6
8, 3
3, 4
5, 5
8, 9""".splitlines()
    distances_between_points(input)



if __name__ == "__main__":
    main()
