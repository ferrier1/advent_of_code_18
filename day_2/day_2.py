from collections import Counter
from itertools import combinations
import difflib


def readin(file):
    with open(file) as f:
        changes = f.read().splitlines()
        return changes


def checksum(box_ids):
    two = 0
    three = 0
    for id in box_ids:
        count = Counter(id)
        l = [x for x in count.values()]
        if 2 in l and 3 in l:
            two += 1
            three += 1
        elif 2 in l:
            two += 1
        elif 3 in l:
            three += 1
        else:
            pass
    return(two * three)


def finder(input):
    final = []
    d = difflib.Differ()
    combs = combinations(input, 2)
    for row in combs:
        diff_list = []
        for letter in range(len(row[0])):
            diff = d.compare(row[0][letter], row[1][letter])
            diff_str = ''.join(diff)
            if '-' not in diff_str:
                diff_list.append(diff_str)
        if diff_list:
            final.append(''.join(diff_list).replace(' ', ''))
    return max(final, key=len)


def main():
    input = readin('inputs/input.txt')
    #input = ['abcde', 'fghij', 'klmno', 'pqrst', 'fguij', 'axcye', 'wvxyz']
    print(checksum(input))
    print(finder(input))



if __name__ == "__main__":
    main()
