from collections import Counter

def readin(file):
    with open(file) as f:
        changes = f.read().splitlines()
        return changes



def checksum(box_ids):
    two_list = 0
    three_list = 0
    for id in box_ids:
        count = Counter(id)
        for letter in count:
            if count[letter] == 2:
                two_list += 1
                print(id, 2)
            elif count[letter] == 3:
                print(id, 3)
                three_list += 1
            else:
                pass
    print(two_list, three_list)






def main():
    #input = readin('inputs/input.txt')
    input = ['bababc', 'abcdef', 'abbcde', 'abcccd', 'aabcdd', 'abcdee', 'ababab']
    print(checksum(input))



if __name__ == "__main__":
    main()
