


def readin(file):
    with open(file) as f:
        changes = f.read().splitlines()
        return changes


def solver(claims):
    for claim in claims:
        parse = claim.split(" ")
        corner_coord = parse[2].strip(":").split(",")
        size = parse[3].split("x")
        print(corner_coord, size)






def main():
    input = readin('inputs/input.txt')
    solver(input)



if __name__ == "__main__":
    main()
