n = int(input("Please input month: "))
ans = (30000 - 1250 * (n - 1)) * 0.005 + 1250
print("%.2f" % ans)
