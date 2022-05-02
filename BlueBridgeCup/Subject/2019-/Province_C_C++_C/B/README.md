[](./image/img.png)

题目链接：[https://www.lanqiao.cn/courses/2786/learning/?id=67815](https://www.lanqiao.cn/courses/2786/learning/?id=67815)

## Ideas

对于一个矩形来说，能切割下来的正方形肯定是以较短的那条边为边长，然后切出来一个正方形，然后长边要减去短边，直到两边相等为止。

## Code

```python
if __name__ == '__main__':
    a, b, ans = 2019, 324, 0
    while a != b:
        ans += 1
        if a > b:
            a -= b
            print(f"切一个 {b} * {b} 的正方形")
        elif a < b:
            b -= a
            print(f"切一个 {a} * {a} 的正方形")
    else:
        print(f"剩一个 {a} * {a} 的正方形")
        ans += 1
    print(f"ans = {ans}")
```

## Answer: 21