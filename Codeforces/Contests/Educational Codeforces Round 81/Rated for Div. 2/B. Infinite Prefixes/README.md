# B. Infinite Prefixes

# B、 无限前缀

You are given string s of length n consisting of 0-s and 1-s.

给出了长度为n的字符串s，由0-s和1-s组成。

You build an infinite string t as a concatenation of an infinite number of strings s, or t=ssss…

您构建一个无限字符串t作为无穷多个字符串s的连接，或者t=sss…

For example, if s= 10010, then t= 100101001010010...

例如，如果s=10010，则t=100101001010010。。。

Calculate the number of prefixes of t with balance equal to x.

计算t的前缀个数，余数等于x。

The balance of some string q is equal to cnt0,q−cnt1,q, where cnt0,q is the number of occurrences of 0 in q, and cnt1,q is the number of occurrences of 1 in q.

一些字符串q的平衡等于cnt<sub>0，q</sub>−cnt<sub>1，q</sub>，其中cnt<sub>0，q</sub>是q中0的出现次数，cnt<sub>1，q</sub>是q中1的出现次数。

The number of such prefixes can be infinite; if it is so, you must say that.

这样的前缀的数目可以是无限的；如果是这样的话，你必须这么说。

The empty prefix is a valid prefix of t.

空前缀是t的有效前缀。

## Input

## 输入

The first line contains the single integer T (1≤T≤100) — the number of test cases.

第一行包含单个整数T（1≤T≤100）-测试用例的数量。

Next 2T lines contain descriptions of test cases — two lines per test case.

接下来的2T行包含测试用例的描述-每个测试用例两行。

The first line contains two integers n and x (1≤n≤10<sup>5</sup>, -10<sup>9</sup>≤x≤10<sup>9</sup>) — the length of string s and the desired balance, respectively.

第一行包含两个整数n和x（1≤n≤10<sup>5</sup>，-10<sup>9</sup>≤x≤10<sup>9</sup>）-分别是字符串s的长度和所需的平衡。

The second line contains the binary string s (|s|=n, si∈{0,1}).

第二行包含二进制字符串s（| s |=n，si∈{0,1}）。

It's guaranteed that the total sum of n doesn't exceed 10<sup>5</sup>.

保证n的总和不超过10<sup>5</sup>。

## Output

## 输出

Print T integers — one per test case.

打印T整数-每个测试用例一个。

For each test case print the number of prefixes or −1 if there is an infinite number of such prefixes.

对于每个测试用例，打印前缀的数量，如果有无限多的前缀，则打印-1。