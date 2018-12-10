import string

def readin(file):
    with open(file) as f:
        input = f.read().strip()
        return list(input)


def grouper(input):
    groups = [input[i:i+2] for i in range(len(input))]
    #return groups
    print(groups)

def is_match(letter_1, letter_2):
        if letter_1 == letter_2:
            return False
        elif letter_1 == letter_2.lower():
            return True
        elif letter_1 == letter_2.upper():
            return True
        else:
            return False

"""
def solver(input):
    for x in range(len(input)):
        idx = 0
        for letter in input:
            try:
                if is_match(input[idx], input[idx+1]):
                    input.pop(idx)
                    input.pop(idx)
            except:
                pass
            idx += 1
    return len(input)
"""

def solver(input):
    stack = []

    for c in input:
        if len(stack) > 0 and is_match(stack[-1], c):
            stack.pop()
        else:
            stack.append(c)
    return len(stack)

def part_2(input):
    removal_lengths = []
    for letter in string.ascii_lowercase:
        for c in input:
            if c == letter or c == letter.upper():
                input.remove(c)
        length = [solver(input), letter]
        removal_lengths.append(length)
    lowest = sorted(removal_lengths)
    print(lowest)



def main():
    input = readin('inputs/input.txt')
    #input = list('dabAcCaCBAcCcaDA')
    print(solver(input))
    print(part_2(input))







if __name__ == "__main__":
    main()
