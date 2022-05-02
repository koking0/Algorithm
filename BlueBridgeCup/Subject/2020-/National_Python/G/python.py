from collections import Counter


if __name__ == '__main__':
    ans = 0
    k = int(input())
    string = input()
    string_list = [string[i: i + k] for i in range(0, len(string), k)]

    for i in range(k):
        cnt = Counter()
        for j in range(len(string_list)):
            cnt[string_list[j][i]] += 1
        ans += len(string_list) - cnt.most_common(1)[0][1]
    print(ans)
