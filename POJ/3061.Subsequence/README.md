# Subsequence POJ - 3061

A sequence of N positive integers (10 < N < 100 000), each of them less than or equal 10000, and a positive integer S (S < 100 000 000) are given.

给出了N个正整数（10<N<100000）的序列，每个正整数小于或等于10000，以及一个正整数S（S<100000 000）。

Write a program to find the minimal length of the subsequence of consecutive elements of the sequence, the sum of which is greater than or equal to S.

编写一个程序，找出序列中连续元素的子序列的最小长度，其和大于或等于S。

## Input

## 输入

The first line is the number of test cases.

第一行是测试用例的数量。

For each test case the program has to read the numbers N and S, separated by an interval, from the first line.

对于每个测试用例，程序必须从第一行读取数字N和S，用间隔隔开。

The numbers of the sequence are given in the second line of the test case, separated by intervals.

序列号在测试用例的第二行给出，用间隔隔开。

The input will finish with the end of file.

输入将在文件结束时结束。

## Output

## 输出

For each the case the program has to print the result on separate line of the output file.if no answer, print 0.

对于每种情况，程序必须在输出文件的单独行上打印结果。如果没有答案，则打印0。

## Sample Input
2
10 15
5 1 3 5 10 7 4 9 2 8
5 11
1 2 3 4 5

## Sample Output
2
3

## 思路

用两个指针，从序列头出发，分别表示区间的头和尾。

当前区间和小于目标值时，尾指针右移；

当前区间和大于等于目标值时，先试着更新答案，然后头指针右移。

通过移动头尾指针，遍历一个数列，从而求解一个问题的的算法，就是尺取法。

因为整个过程将数列从头到尾遍历了一遍，所以尺取法的时间复杂度为O(n)。