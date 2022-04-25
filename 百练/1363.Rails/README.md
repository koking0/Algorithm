题目链接：[https://vjudge.net/problem/OpenJ_Bailian-1363](https://vjudge.net/problem/OpenJ_Bailian-1363)

## Ideas

一道挺明显的栈的应用题目。

给定一个数字 n，那么进栈的顺序就确定了，就是：1, 2, ..., N。

但并不是一下全部入栈，而是我们要检查题目给定的出栈顺序，如果出现能够跟出栈顺序匹配上的数字，那么就按照出栈顺序出栈，否则就继续入栈。

如果所有的元素都入栈了，结果出栈顺序还没有检查完，那就说明此出栈顺序进非法。

## Code

### Python

```python
if __name__ == '__main__':
    n = int(input())
    while n != 0:
        while True:
            pop_list = list(map(int, input().split(' ')))
            if pop_list[0] == 0:
                break
            idx, stack = 0, []
            for i in range(1, n + 1):
                stack.append(i)
                while stack and stack[-1] == pop_list[idx]:
                    idx += 1
                    stack.pop()
            if idx == n:
                print("Yes")
            else:
                print("No")
        print()
        n = int(input())
```