for a in range(1, int(1000 ** 0.5)):
    for b in range(a + 1, int(1000 ** 0.5)):
        for c in range(b + 1, int(1000 ** 0.5)):
            if a ** 2 + b ** 2 + c ** 2 == 1000:
                print(f"{a} ^ 2 + {b} ^ 2 + {c} ^ 2 = 1000")
