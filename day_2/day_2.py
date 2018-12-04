from collections import Counter

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






def main():
    input = readin('inputs/input.txt')
    #input = ['abcdef', 'bababc', 'abbcde', 'abcccd', 'aabcdd', 'abcdee', 'ababab']
    print(checksum(input))



if __name__ == "__main__":
    main()
