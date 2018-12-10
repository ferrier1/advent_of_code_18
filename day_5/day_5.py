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


def solver(input):
    stack = []

    for char in input:
        if len(stack) > 0 and is_match(stack[-1], char):
            stack.pop()
        else:
            stack.append(char)
    return len(stack)

def solver_part_2(input, letter):
    stack = []

    for char in input:
        if char == letter:
            pass
        elif char == letter.upper():
            pass
        elif len(stack) > 0 and is_match(stack[-1], char):
            stack.pop()
        else:
            stack.append(char)
    return [len(stack), letter]



def main():
    part_2 = []
    input = readin('inputs/input.txt')
    #input = list('dabAcCaCBAcCcaDA')
    for letter in string.ascii_lowercase:
        part_2.append([solver_part_2(input, letter)])
    print(sorted(part_2))







if __name__ == "__main__":
    main()
