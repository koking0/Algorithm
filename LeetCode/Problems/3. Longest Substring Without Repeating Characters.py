'''
Given a string, find the length of the longest substring without repeating characters.

给定一个字符串，找到最长子字符串的长度而不重复字符。
'''


class Solution:
    def lengthOfLongestSubstring(self, s):
        dicts = {}
        maxlength = start = 0
        for i in range(len(s)):
            if s[i] in dicts:
                start = max(dicts[s[i]] + 1, start)    # 从重复单词的下一个位置开始
            maxlength = max(i - start + 1, maxlength)   
            dicts[s[i]] = i
        return maxlength


a = Solution()
print(a.lengthOfLongestSubstring("pwwkew"))