from typing import List


class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
        """
        找到一个时间长度为 X 的窗口包含最多原本因为老板生气而不满意的顾客（Sliding Window）
        ans = 老板不生气时间内的顾客总数（customer1） + 窗口 X 内的原本不满意的顾客（customer2）
        """
        n = len(customers)
        customer1 = sum(customers[i] * (1 - grumpy[i]) for i in range(n))
        customer2 = customer_x = sum(customers[i] * grumpy[i] for i in range(X))
        for i in range(X, n):
            customer_x = customer_x + customers[i] * grumpy[i] - customers[i - X] * grumpy[i - X]
            customer2 = max(customer2, customer_x)
        return customer1 + customer2


if __name__ == '__main__':
    s = Solution()
    print(s.maxSatisfied(customers=[1, 0, 1, 2, 1, 1, 7, 5], grumpy=[0, 1, 0, 1, 0, 1, 0, 1], X=3))
