from itertools import permutations

if __name__ == '__main__':
    for item in permutations(range(1, 10)):
        A = item[0] * 100 + item[1] * 10 + item[2]
        B = item[3] * 100 + item[4] * 10 + item[5]
        C = item[6] * 100 + item[7] * 10 + item[8]
        if B == 2 * A and C == 3 * A:
            print(f"A = {A}, B = {B}, C = {C}")
