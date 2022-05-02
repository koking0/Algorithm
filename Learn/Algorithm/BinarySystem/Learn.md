# 进制转换

## 为什么要学习进制

计算机只认识二进制，也就是0和1,为了更好学习计算机，首先就要深入理解什么是进制。

当初最早的程序员都是靠二进制写程序的，就是一堆人敲键盘的0和1来写程序。

后来过渡到十六进制，大家都在敲0,1,2,3,4,5,6,7,8,9,a,b,c,d,e,f来写程序。

二进制使用起来很不方便， 16进制或8进制可以解决这个问题，因为，进制越大，数的表达长度也就越短。

为什么偏偏是16或8进制，而不其它的?

2、8、16，分别是2的1次方、3次方、4次方。

这一点使得三种进制之间可以非常直接地互相转换。

8进制或16进制缩短了二进制数，但保持了二进制数的表达特点。

可以明显地看到二进制只能写2个数，而十六进制可以写16个数，这大大地提高了编程的效率。

软件在编译器里是2进制的，在编辑器里是十六进制的，我们写的程序被编译器从十六进制转换成了二进制，多么牛逼啊！

## 不同进制之间的转换

## 十进制转二进制

首先从我们最熟悉的十进制和计算机最喜欢的二进制之间的转换开始。

给定一个十进制整数，要求转换为二进制。

首先要理解十进制转换为二进制的流程。

高中的时候就应该已经接触过了，总结起来一句话就是除2取余。

    假设给定一个数7：
    
        1.7 / 2 = 3......1
        2.3 / 2 = 1......1
        3.1 / 2 = 0......1
    
    所以，十进制7 = 二进制111
    
    再看一个更大的数13：
    
        1.13 / 2 = 6......1
        2.6  / 2 = 3......0
        3.3  / 2 = 1......1
        4.1  / 2 = 0......1
        
    所以，十进制13 = 二进制1101

所以，十进制转二进制就是要用代码逻辑模拟这个流程：

```python
num_10 = int(input())  # 输入的十进制数
num_2 = []      # 其他语言可以用数组

while num_10:     # 不明确循环次数的时候用while循环
    num_2.append(num_10 % 2)    # 将除2取余的结果添加到列表中
    num_10 = int(num_10 / 2)    # 将十进制数除以2

print("".join(map(str, num_2[::-1])))
```

## 二进制转十进制

给定一个二进制数字符串，要求转换为十进制数。

首先要理解二进制转换为十进制的流程。

高中的时候也已经接触过了，方法是：权相加法。

    假设给定一个二进制数111：
    
        1 * 2 ^ 0 + 1 * 2 ^ 1 + 1 * 2 ^ 2
        = 1 + 2 + 4
        = 7
    
    所以，二进制111 = 十进制7
    
    再看一个更大的数1101：
    
        1 * 2 ^ 0 + 0 * 2 ^ 1 + 1 * 2 ^ 2 + 1 * 2 ^ 3
        = 1 + 0 + 4 + 8
        = 13
        
    所以，二进制1101 = 十进制13
    
所以，二进制转十进制就是要用代码逻辑模拟这个流程：

```python
num_2 = input()     # 输入的二进制数字符串
num_10 = 0

for i in range(len(num_2)):     # 明确循环次数的时候用for循环
    num_10 += int(num_2[::-1][i]) * (2 ** i)

print(num_10)
```

## 十进制转任意进制

类似于十进制转二进制，十进制转任意进制就是除any取余。

```python
import string


num_10 = int(input("输入的十进制数:"))
base = int(input("输入要转换为的进制:"))
num_any = []      # 其他语言可以用数组

while num_10:     # 不明确循环次数的时候用while循环
    num_any.append(num_10 % base)  # 将除2取余的结果添加到列表中
    num_10 = int(num_10 / base)    # 将十进制数除以2

char = list(string.ascii_uppercase)         # 26大写英文字母集
for i in range(len(num_any)):
    if num_any[i] > 9:                      # 如果数字大于两位
        num_any[i] = char[num_any[i] - 10]  # 转换为相应的字母
print("".join(map(str, num_any[::-1])))
```

验证网站：https://tool.oschina.net/hexconvert/

## 任意进制转十进制

类似于二进制转十进制，任意进制转十进制也是权相加法。

```python
base = int(input("请输入任意进制："))
num_any = input("请输入的任意进制数字符串：")
num_10 = 0

num_any = list(num_any.upper())
for i in range(len(num_any)):
    if num_any[i].isalpha():     # 如果当前元素为字母
        num_any[i] = ord(num_any[i]) - ord("A") + 10  # 转换为相应的数字
        
for i in range(len(num_any)):     # 明确循环次数的时候用for循环
    num_10 += int(num_any[::-1][i]) * (base ** i)

print(num_10)
```

验证网站：https://tool.oschina.net/hexconvert/

## M进制转N进制

学会了十进制转任意进制和任意进制转十进制之后就可以做任意的M进制转任意的N进制。

M进制转换为N进制：先由M进制转换为10进制，再由10进制转换为N进制。

```python
import string


m = int(input("M = "))
num_m = input("M number = ")
n = int(input("N = "))

num_10 = 0
num_m = list(num_m.upper())
for i in range(len(num_m)):
    if num_m[i].isalpha():     # 如果当前元素为字母
        num_m[i] = ord(num_m[i]) - ord("A") + 10  # 转换为相应的数字

for i in range(len(num_m)):     # 明确循环次数的时候用for循环
    num_10 += int(num_m[::-1][i]) * (m ** i)

num_n = []      # 其他语言可以用数组
while num_10:     # 不明确循环次数的时候用while循环
    num_n.append(num_10 % n)  # 将除2取余的结果添加到列表中
    num_10 = int(num_10 / n)    # 将十进制数除以2

char = list(string.ascii_uppercase)         # 26大写英文字母集
for i in range(len(num_n)):
    if num_n[i] > 9:                      # 如果数字大于两位
        num_n[i] = char[num_n[i] - 10]  # 转换为相应的字母
print("N number =", "".join(map(str, num_n[::-1])))
```

# Python进制转换内置函数


|	|2进制|	8进制|	10进制|	16进制|
|:-:|:-:|:-:|:-:|:-:|
|2进制	|-	            |bin(int(x, 8))	|bin(int(x, 10))	|bin(int(x, 16))|
|8进制	|oct(int(x, 2))	|-	            |oct(int(x, 10))	|oct(int(x, 16))|
|10进制	|int(x, 2)	    |int(x, 8)	    |-	                |int(x, 16)|
|16进制	|hex(int(x, 2))	|hex(int(x, 8))	|hex(int(x, 10))	|-|