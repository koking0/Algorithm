S = input()
T = input()

indexS, indexT = 0, 0
while indexT < len(T):
    if indexS == len(S):
        break

    if S[indexS] == T[indexT]:
        indexS += 1
        indexT += 1
    else:
        indexS += 1
print(indexT)
