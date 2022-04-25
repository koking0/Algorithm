# A. Display The Number

# A、 显示号码

You have a large electronic screen which can display up to 998244353 decimal digits.

您有一个大的电子屏幕，可以显示高达998244353**位**小数。

The digits are displayed in the same way as on different electronic alarm clocks: each place for a digit consists of 7 segments which can be turned on and off to compose different digits.

数字的显示方式与在不同电子闹钟上的显示方式相同：一个数字的每个位置由7个段组成，这些段可以打开和关闭以组成不同的数字。

The following picture describes how you can display all 10 decimal digits:

下图描述了如何显示所有10位十进制数字：

![](https://espresso.codeforces.com/39cedf07ce9ef18d7ec074f319640a9857b9f8cb.png)

As you can see, different digits may require different number of segments to be turned on.

如您所见，不同的数字可能需要启用不同数量的段。

For example, if you want to display 1, you have to turn on 2 segments of the screen, and if you want to display 8, all 7 segments of some place to display a digit should be turned on.

例如，如果要显示1，则必须打开屏幕的2个部分；如果要显示8，则应打开某个地方显示数字的所有7个部分。

You want to display a really large integer on the screen.

你想在屏幕上显示一个非常大的整数。

Unfortunately, the screen is bugged: no more than n segments can be turned on simultaneously.

不幸的是，屏幕被窃听：不能同时打开超过n个段。

So now you wonder what is the greatest integer that can be displayed by turning on no more than n segments.

所以现在你想知道什么是最大的整数，可以通过打开不超过n段显示。

Your program should be able to process t different test cases.

你的程序应该能够处理t个不同的测试用例。

## Input

## 输入

The first line contains one integer t (1≤t≤100) — the number of test cases in the input.

第一行包含一个整数t（1≤t≤100）-输入中的测试用例数。

Then the test cases follow, each of them is represented by a separate line containing one integer n (2≤n≤105) — the maximum number of segments that can be turned on in the corresponding testcase.

然后测试用例跟随，每一个都由一个独立的行表示，其中包含一个整数N（2≤n≤10<sup>5</sup>）-在相应的测试用例中可以打开的最大段数。

It is guaranteed that the sum of n over all test cases in the input does not exceed 105.

保证输入中所有测试用例的n之和不超过10<sup>5</sup>。

## Output

## 输出

For each test case, print the greatest integer that can be displayed by turning on no more than n segments of the screen.

对于每个测试用例，打印可以通过打开不超过n个屏幕段显示的最大整数。

Note that the answer may not fit in the standard 32-bit or 64-bit integral data type.

请注意，答案可能不适合标准的32位或64位整数数据类型。

# 思路

**“可以显示高达998244353位小数”**

我一开始以为这是限制显示位数，最多只能显示9位数。

结果最后发现理解错了，他说的是最多能显示的位数。

|数字|0|1|2|3|4|5|6|7|8|9|
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
|段数|6|2|5|6|4|5|6|3|7|6|

这是组成每个数字需要的段数，最少需要2段能组成一个数字1，除此之外最少需要3段能组成一个数字7.