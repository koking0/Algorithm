# -*- coding: utf-8 -*-
# @Author   : Alex
# @Time     : 2022/5/5 17:56
# @File     : ZJ1附加题.py
# @Software : PyCharm
# Email     : liu_zhao_feng_alex@163.com
# Blog      : https://alex007.blog.csdn.net/
if __name__ == '__main__':
	n = int(input())
	transfer_list = list(map(int, input().split()))
	dp = [float("inf")] * (n + 1)
	dp[0] = 0
	
	mod = 1000000007
	for i in range(1, n + 1):
		dp[i] = (dp[i - 1] + (dp[i - 1] - dp[transfer_list[i - 1] - 1] + 1) + 1) % mod
	print(dp[-1])
