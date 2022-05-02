Given a non-empty string s, you may delete at most one character.
给定一个非空字符串，您最多可以删除一个字符。

Judge whether you can make it a palindrome.
判断你是否能把它变成回文。

Example 1:

Input: "aba"
Output: True

Example 2:

Input: "abca"
Output: True

Explanation: You could delete the character 'c'.

Note:
The string will only contain lowercase characters a-z.

The maximum length of the string is 50000.

## 思路

#### 1

首先判断字符串是不是回文串，如果是直接返回True。

如果不是，继续下面步骤：

两个指针，分别从字符串的头和尾向中间移动。

如果两个指针指向的字符不相等，分别判断去掉两个指针所在的字符后是不是回文。

**例：aba**

int(len(s) / 2) = 1

第一次循环：i = 0, -(i + 1) = -1 

**例：abba**

int(len(s) / 2) = 2

第一次循环：i = 0, -(i + 1) = -1

第二次循环：i = 1, -(i + 1) = -2  

## 最终AC思路

直接用s[::-1]翻转字符串就可以判断字符串是否回文

从头和尾相向遍历整个字符串，如果遇到不等的位置：

将字符串分别去掉从头到i + 1位置和-i到尾部和从头去掉到i和-i-1到尾部