'''
Given an array of integers, return indices of the two numbers such that they add up to a specific target.  You may assume that each input would have exactly one solution, and you may not use the same element twice.

给定一个整数数组，返回两个数字的索引，以便它们加起来成为一个特定的目标。 您可以假定每个输入都只有一个解决方案，并且您可能不会两次使用同一元素。
'''

'''
描述
enumerate() 函数用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，同时列出数据和数据下标，一般用在 for 循环当中。

语法
enumerate(sequence, [start=0])

参数
sequence -- 一个序列、迭代器或其他支持迭代对象。
start -- 下标起始位置。

返回值
返回 enumerate(枚举) 对象。
'''
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        for i in range(len(nums)):
            if target - nums[i] not in dict:
                # 如果目标值不在dict中，在dict中将当前值位置更新为索引
                dict[nums[i]] = i
            else:
                # 如果目标值在dict中，则返回目标值在dict中的索引和当前值的索引
                return [dict[target-nums[i]], i]
