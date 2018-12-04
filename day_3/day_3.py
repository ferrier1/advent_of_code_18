


def readin(file):
    with open(file) as f:
        changes = f.read().splitlines()
        return changes









def main():
    input = readin('inputs/input.txt')
    print(input)


if __name__ == "__main__":
    main()
