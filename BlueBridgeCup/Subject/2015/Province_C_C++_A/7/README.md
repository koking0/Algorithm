## 手链样式

小明有3颗红珊瑚，4颗白珊瑚，5颗黄玛瑙。

他想用它们串成一圈作为手链，送给女朋友。

现在小明想知道：如果考虑手链可以随意转动或翻转，一共可以有多少不同的组合样式呢？

请你提交该整数。

不要填写任何多余的内容或说明性的文字。

## Ideas

这是一个排列组合问题，一共有 12 个位置，可以先从中选出 3 个，放红珊瑚，然后从剩下的 9 个中选出 4 个放白珊瑚，剩余的 5 个位置放黄玛瑙。

这道题只是一道填空题，所以可以用一些语言自带的全排列函数，但是需要做一些去重的操作。

手链可以随意转动，相当于将排列进行右移操作，所以将上面的结果除以 12。

手链还能够翻转，也就是说必须保证对称轴两边的石头不同类型数量相等，所以必须由红珊瑚和黄玛瑙作为对称轴。

对称轴两边分别放 5 个石头，从 5 个位置里面选 2 个放白珊瑚，然后从剩下的 3 个位置中选 2 个放黄玛瑙。

考虑到翻转的情况，将上面的结果除以 2，然后再加上一个对称的操作。所以这道题其实是可以通过纯数学计算的方式得出结果的。

不过作为一名勤勤恳恳的码农，不写点代码总觉得难受，所以下面的代码是通过全排列+去重的方式实现的。

## Code

### C++

```cpp
#include <iostream>
#include <string>
#include <algorithm>
#include <vector>

using namespace std;

int main(int argc, const char *argv[]) {
    string s = "aaabbbbccccc";
    vector<string> v1;
    int ans = 0;
    do {
        //排出重复，对于v1中的每个元素进行检查，如果存在s的旋转或者翻转，则跳过
        int i = 0;
        for (; i < v1.size(); ++i) {
            if (v1[i].find(s) != string::npos)
                break;
        }
        //s不可用的情况
        if (i != v1.size())
            continue;
        string s2 = s + s;
        v1.push_back(s2);//用于判断旋转的情况
        reverse(s2.begin(), s2.end());
        v1.push_back(s2);//将s的翻转放入vector中

        ans++;
    } while (next_permutation(s.begin(), s.end()));
    cout << ans << endl;
    return 0;
}
```

### Python

```python
from itertools import permutations

if __name__ == '__main__':
    ans, cnt = set(), 0
    nums = ['1', '1', '1', '2', '2', '2', '2', '3', '3', '3', '3', '3']
    for item in permutations(nums):
        string = ''.join(item)
        if string not in ans:  # 如果这种样式之前已经遇到过
            print(string)
            string2 = string + string
            for i in range(len(nums)):
                ans.add(string2[i:i + 12])
            string2 = string2[::-1]  # 考虑翻转的情况
            for i in range(len(nums)):
                ans.add(string2[i:i + 12])
            cnt += 1
    print(cnt)
```

## Answer: 1170