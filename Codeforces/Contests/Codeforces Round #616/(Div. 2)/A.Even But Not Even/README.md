# A. Even But Not Even

# A.偶但不偶

time limit per test1 second

每次测试的时限1秒

memory limit per test256 megabytes

每个测试的内存限制256 MB

inputstandard input

输入标准输入

outputstandard output

输出标准输出

Let's define a number ebne (even but not even) if and only if its sum of digits is divisible by 2 but the number itself is not divisible by 2. 

让我们定义一个数字ebne（偶数，但不是偶数），当且仅当它的数字总和可以被2整除但数字本身不能被2整除时。

For example, 13, 1227, 185217 are ebne numbers, while 12, 2, 177013, 265918 are not.

例如，13，1227，185217是ebne数，而12，2，177013，265918不是。

If you're still unsure what ebne numbers are, you can look at the sample notes for more clarification.

如果仍然不确定ebne数是多少，可以查看样本注释以进一步了解。

You are given a non-negative integer s, consisting of n digits. 

您会得到一个非负整数s，它由n个数字组成。

You can delete some digits (they are not necessary consecutive/successive) to make the given number ebne. 

您可以删除一些数字（它们不必是连续的/连续的），以使给定的数字为ebne。

You cannot change the order of the digits, that is, after deleting the digits the remaining digits collapse. 

您无法更改数字的顺序，也就是说，删除数字后，其余数字将折叠。

The resulting number shouldn't contain leading zeros. 

结果数字不应包含前导零。

You can delete any number of digits between 0 (do not delete any digits at all) and n−1.

您可以删除0（根本不删除任何数字）和n-1之间的任何数字。

For example, if you are given s=222373204424185217171912 then one of possible ways to make it ebne is: 222373204424185217171912 → 2237344218521717191. 

例如，如果给定s = 222373204424185217171912，那么使它生效的一种可能方法是：222373204424185217171912→2237344218521717191。

The sum of digits of 2237344218521717191 is equal to 70 and is divisible by 2, but number itself is not divisible by 2: it means that the resulting number is ebne.

2237344218521717191的数字总和等于70，并且可以被2整除，但是数字本身不能被2整除，这意味着所得的数字是ebne。

Find any resulting number that is ebne. 

查找任何结果为ebne的数字。

If it's impossible to create an ebne number from the given number report about it.

如果不可能从给定的数字报告中创建ebne数字，则有关它。

## Input

## 输入

The input consists of multiple test cases. 

输入包含多个测试用例。

The first line contains a single integer t (1≤t≤1000)  — the number of test cases. 

第一行包含一个整数t（1≤t≤1000）-测试用例的数量。

The description of the test cases follows.

测试用例的描述如下。

The first line of each test case contains a single integer n (1≤n≤3000)  — the number of digits in the original number.

每个测试用例的第一行包含一个整数n（1≤n≤3000）-原始数字中的位数。

The second line of each test case contains a non-negative integer number s, consisting of n digits.

每个测试用例的第二行包含一个非负整数s，由n个数字组成。

It is guaranteed that s does not contain leading zeros and the sum of n over all test cases does not exceed 3000.

保证s不包含前导零，并且在所有测试用例中n的总和不超过3000。

## Output

## 输出

For each test case given in the input print the answer in the following format:

对于输入中给出的每个测试用例，请按以下格式回答：

If it is impossible to create an ebne number, print "-1" (without quotes);

如果无法创建ebne号，请打印“ -1”（不带引号）；

Otherwise, print the resulting number after deleting some, possibly zero, but not all digits. 

否则，请在删除一些（可能为零，但不是全部）数字后打印结果数字。

This number should be ebne. 

此数字应为ebne。

If there are multiple answers, you can print any of them. 

如果有多个答案，则可以打印其中任何一个。

Note that answers with leading zeros or empty strings are not accepted. 

请注意，不接受带有前导零或空字符串的答案。

It's not necessary to minimize or maximize the number of deleted digits.

不必最小化或最大化已删除数字的数量。