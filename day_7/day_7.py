

def readin(file):
    with open(file) as f:
        input = f.read().splitlines()
        return input








def main():
    input = readin('inputs/input1.txt')
    print(input)





if __name__ == "__main__":
    main()