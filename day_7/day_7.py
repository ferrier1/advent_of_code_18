from collections import defaultdict

def readin(file):
    with open(file) as f:
        input = f.read().splitlines()
        return input


def parser(input):
    a, b = [],[]
    for step in input:
        a.append(step[5])
        b.append(step[36])
    return a, b


def start(input):
    start_candidates = []
    data = parser(input)
    for letter in data[0]:
        if letter not in data[1]:
            start_candidates.append(letter)
    return sorted(start_candidates)[0]
    

def solver(input):
    data = parser(input)
    potential_next_steps = defaultdict(list)
    completed_steps = []
    completed_steps.append(start(input))
    idx = 0
    for constraint in data[0]:
        if constraint in completed_steps:
             potential_next_steps[constraint].append(data[1][idx])
        idx += 1
        
    print(potential_next_steps)




def main():
    input = readin('inputs/input1.txt')
    solver(input)
    





if __name__ == "__main__":
    main()