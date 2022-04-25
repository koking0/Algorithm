from typing import List


class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        if n < 2:
            return False

        sum_num = 0
        hash_table = {0: -1}
        for i in range(n):
            sum_num = (sum_num + nums[i]) % k
            if hash_table.get(sum_num, None):
                pre_index = hash_table[sum_num]
                if i - pre_index > 1:
                    return True
            else:
                hash_table[sum_num] = i
        return False
