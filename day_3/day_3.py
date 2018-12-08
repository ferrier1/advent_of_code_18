from collections import defaultdict

def readin(file):
    with open(file) as f:
        changes = f.read().splitlines()
        return changes


def solver(claims):
    used_inches = defaultdict(list)
    duplicates = 0
    for claim in claims:
        parse = claim.split(" ")
        top_left_corner = parse[2].strip(":").split(",")
        size = parse[3].split("x")
        for y in range(int(size[0])):
            for x in range(int(size[1])):
                inch = (int(top_left_corner[0]) + y, int(top_left_corner[1]) + x)
                used_inches[inch].append(parse[0])
    for item in used_inches:
        if len(used_inches[item]) >= 2:
            duplicates += 1
    return duplicates









def main():
    #input = ["#1 @ 1,3: 4x4", "#2 @ 3,1: 4x4", "#3 @ 5,5: 2x2"]
    input = readin('inputs/input.txt')
    print(solver(input))



if __name__ == "__main__":
    main()
