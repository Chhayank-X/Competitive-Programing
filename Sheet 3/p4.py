for i in range(1, 6, 2):
    s = '1'
    for j in range(3, i + 1, 2):
        s += f' * {j}'
    print(s)
