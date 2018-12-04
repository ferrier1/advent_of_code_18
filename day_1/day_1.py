from collections import Counter
import itertools


def readin(file):
    with open(file) as f:
        changes = f.read().splitlines()
        return changes

"""
def solver(counter, list_of_changes):
    list_of_changes.insert(0, counter)
    lst = list(map(int, list_of_changes))
    print(sum(lst))
"""

def solver(counter, list_of_changes):
    frequencies = []
    for change in list_of_changes:
        if change[0] == '+':
            counter += int(change[1:])
            frequencies.append(counter)
        elif change[0] == '-':
            counter -= int(change[1:])
            frequencies.append(counter)
        else:
            break
    return frequencies



def calibrator(start_list, input):
    duplicate_list = start_list
    ans = start_list
    while True:
        ans = solver(ans[-1], input)
        for num in ans:
            if num not in duplicate_list:
                duplicate_list.append(num)
                print(num)
            else:
                return num


def main():
    input = readin('inputs/input.txt')
    #input = ["+3", "+3", "+4", "-2", "-4"]
    ans = solver(0, input)
    print("part 1 answer is {}".format(ans[-1]))


    print(calibrator(ans, input))





if __name__ == "__main__":
    main()
