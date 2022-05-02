from collections import Counter

if __name__ == '__main__':
    string = input()
    counter = Counter(string)
    counter = sorted(counter.items(), key=lambda x: (-x[1], x[0]))
    for item in counter[0]:
        print(item)
