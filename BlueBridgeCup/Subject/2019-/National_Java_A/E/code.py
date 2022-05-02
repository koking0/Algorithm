import itertools


# 完全平方筛，返回小于等于n的所有完全平方数
def completeSquareSieve(n: int):
    ans, index = [], 0
    while True:
        ans.append(index ** 2)
        index += 1
        if index ** 2 > n:
            break
    return ans

def check(nums):
    for i in nums:
        if i in completeSquareNumbers:
            return False
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] in completeSquareNumbers:
                return False
    return True


ans, completeSquareNumbers = [], completeSquareSieve(200)
for i in range(1, 101):
    if i in completeSquareNumbers:
        continue

    for it in ans:
        if it + i in completeSquareNumbers:
            break
    else:
        ans.append(i)
print(ans)
print(len(ans))
print(check(ans))
