if __name__ == '__main__':
    achievements = []
    n = int(input())
    for _ in range(n):
        achievements.append(int(input()))
    print(max(achievements))
    print(min(achievements))
    print(round(sum(achievements) / len(achievements), 2))
