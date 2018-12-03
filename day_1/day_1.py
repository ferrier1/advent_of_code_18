
def readin(file):
    with open(file) as f:
        changes = f.read().splitlines()
        return changes

def solver(list_of_changes):
    counter = 0
    for change in list_of_changes:
        if change[0] == '+':
            counter += int(change[1:])
        elif change[0] == '-':
            counter -= int(change[1:])
        else:
            break
    print(counter)




def main():
    solver(readin('inputs/input.txt'))


if __name__ == "__main__":
    main()
