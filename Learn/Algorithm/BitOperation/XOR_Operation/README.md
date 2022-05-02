# 异或运算

异或运算就是无进位相加。

0+0=0、1+0=1、0+1=1、1+1=0 (1+1=10，舍弃进位的1)

## 性质

**0^N=N、N^N=0**

**异或运算满足交换律和结合律**

交换律：a^b=b^a

结合律：(a^b)^c = a^(b^c) 

## 扩展

**不用额外变量交换两个数**

```python
import random

a = random.randint(0, 100)
b = random.randint(0, 100)
print("a = ", a, " b = ", b)
a = a ^ b
b = a ^ b
a = a ^ b
print("a = ", a, " b = ", b)
```

```
a =  76  b =  47
a =  47  b =  76
```

**证明：**

假设a的值为x，b的值为y：

1.a = a ^ b ——> a = x ^ y、b = y 

2.b = a ^ b ——> a = x ^ y、b = a ^ y = x ^ y ^y = x

3.a = a ^ b ——> a = x ^ y ^ x = y、b = x

**一个数组中有一个数出现了奇数次，其它数都出现了偶数次，找到这个数**

```python
def odd_times_num1(array):
    eor = 0
    for num in array:
        eor = eor ^ num
    return eor
```

**一个数组中有两个数出现了奇数次，其它数都出现了偶数次，找到这个数**

```python
def odd_times_num2(array):
    eor1 = 0
    for num in array:
        eor1 = eor1 ^ num

    cur, eor2 = eor1 & (~eor1 + 1), 0
    for num in array:
        if cur & num:
            eor2 = eor2 ^ num
    return eor1 ^ eor2, eor2
```