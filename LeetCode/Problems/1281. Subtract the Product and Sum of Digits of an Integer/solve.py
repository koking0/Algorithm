from functools import reduce


class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        nums = list(map(int, list(str(n))))
        product = reduce(lambda a, b: a * b, nums)
        sum_num = sum(nums)
        return product - sum_num


if __name__ == '__main__':
    print(Solution().subtractProductAndSum(234))
