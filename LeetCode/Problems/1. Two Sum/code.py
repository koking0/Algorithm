from typing import List


class Solution:
    def twoSum1(self, nums: List[int], target: int) -> List[int]:
        """暴力枚举"""
        length = len(nums)
        for i in range(length):
            for j in range(i + 1, length):
                if nums[j] == target - nums[i]:
                    return [i, j]

    def twoSum2(self, nums: List[int], target: int) -> List[int]:
        """双通道哈希表"""
        length, values = len(nums), {}
        for i in range(length):
            values[nums[i]] = i
        for i in range(length):
            complement = target - nums[i]
            # 如果补码在数列中并且索引不是自己
            if complement in values and values.get(complement) != i:
                return [i, values.get(complement)]

    def twoSum3(self, nums: List[int], target: int) -> List[int]:
        """单次哈希表"""
        values = {}
        for index in range(len(nums)):
            if target - nums[index] not in values:
                # 如果目标值不在dict中，在dict中将当前值位置更新为索引
                values[nums[index]] = index
            else:
                # 如果目标值在dict中，则返回目标值在dict中的索引和当前值的索引
                return [values[target - nums[index]], index]
