from collections import defaultdict

def readin(file):
    with open(file) as f:
        changes = f.read().splitlines()
        return changes


def solver(claims):
    used_inches = defaultdict(set)
    bad_claim_numbers = set()
    good_claims = {}
    bad_claims = {}
    bad_claims_reverse = {}
    duplicates = 0
    for claim in claims:
        parse = claim.split(" ")
        top_left_corner = parse[2].strip(":").split(",")
        size = parse[3].split("x")
        for y in range(int(size[0])):
            for x in range(int(size[1])):
                inch = (int(top_left_corner[0]) + y, int(top_left_corner[1]) + x)
                used_inches[inch].add(parse[0])
    for k, v in used_inches.items():
        if len(used_inches[k]) >= 2:
            duplicates += 1
            for claims in used_inches[k]:
                bad_claim_numbers.add(claims)
    for k, v in used_inches.items():
        for claim in bad_claim_numbers:
            if claim in used_inches[k]:
                bad_claims[k] = v
    for k, v  in bad_claims.items():
        bad_claims[k] = ''.join(v)
    for k, v  in used_inches.items():
        used_inches[k] = ''.join(v)
    good_claims = set(used_inches.values()) - set(bad_claims.values())
    print(good_claims)
    return duplicates









def main():
    #input = ["#1 @ 1,3: 4x4", "#2 @ 3,1: 4x4", "#3 @ 5,5: 2x2"]
    input = readin('inputs/input.txt')
    print(solver(input))



if __name__ == "__main__":
    main()
