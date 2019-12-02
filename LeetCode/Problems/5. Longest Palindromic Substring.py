# coding=utf-8
'''
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.
给定字符串S，在S中找到最长回文子串，可以假定S的最大长度为1000。

Example 1:

    Input: "babad"
    Output: "bab"
    Note: "aba" is also a valid answer.

Example 2:

    Input: "cbbd"
    Output: "bb"
'''


class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s

        for i in range(int(len(s) / 2)):
            if s[i] != s[len(s) - i -1]:
                break
        else:
            return s
        
        substring = ""

        for i in range(len(s)):
            for j in range(len(s)):
                if j > i:
                    substring_temp = s[i:j]
                    print(substring_temp)
                    
                    for k in range(int(1 + (len(substring_temp)) / 2)):
                        if substring_temp[k] != substring_temp[len(substring_temp) - k -1]:
                            break
                    else:
                        print("enable: ", substring_temp)
                        if len(substring_temp) > len(substring):
                            substring = substring_temp
        return substring

a = Solution()
print(a.longestPalindrome("abb"))
