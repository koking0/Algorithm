for i in range(1, 200 // 1):
    for j in range(1, 200 // 2):
        for k in range(1, 200 // 5):
            if i * 1 + j * 2 + k * 5 == 200 and j == 10 * i:
                print(f'i = {i}, j = {j}, k = {k}, sum = {i + j + k}')
