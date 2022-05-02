from copy import deepcopy

if __name__ == '__main__':
    cards = []
    for c in ['S', 'H', 'C', 'D']:
        for i in range(1, 14):
            cards.append(f"{c}{i}")
    cards.append("J1")
    cards.append("J2")
    # print(cards)

    n = len(cards)
    ans = deepcopy(cards)
    t = int(input())
    orders = list(map(int, input().split()))
    for _ in range(t):
        cards = deepcopy(ans)
        for i in range(n):
            ans[orders[i] - 1] = cards[i]
    print(' '.join(ans))
