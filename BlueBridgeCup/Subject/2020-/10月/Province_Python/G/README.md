试题 G: 单词分析
时间限制: 1.0s 内存限制: 512.0MB 本题总分：20 分

【问题描述】
小蓝正在学习一门神奇的语言，这门语言中的单词都是由小写英文字母组成，有些单词很长，远远超过正常英文单词的长度。
小蓝学了很长时间也记不住一些单词，他准备不再完全记忆这些单词，而是根据单词中哪个字母出现得最多来分辨单词。
现在，请你帮助小蓝，给了一个单词后，帮助他找到出现最多的字母和这个字母出现的次数。

【输入格式】
输入一行包含一个单词，单词只由小写英文字母组成。

【输出格式】
输出两行，第一行包含一个英文字母，表示单词中出现得最多的字母是哪个。
如果有多个字母出现的次数相等，输出字典序最小的那个。
第二行包含一个整数，表示出现得最多的那个字母在单词中出现的次数。

【样例输入】
lanqiao

【样例输出】
a
2

【样例输入】
longlonglongistoolong

【样例输出】
o
6

【评测用例规模与约定】
对于所有的评测用例，输入的单词长度不超过 1000。

## Ideas

这题的价值大概就在于考察计数器和字典排序吧。

## Code

### Python

```python
from collections import Counter

if __name__ == '__main__':
    string = input()
    counter = Counter(string)
    counter = sorted(counter.items(), key=lambda x: (-x[1], x[0]))
    for item in counter[0]:
        print(item)
```

## 在线评测：[https://www.acwing.com/problem/content/3306/](https://www.acwing.com/problem/content/3306/)