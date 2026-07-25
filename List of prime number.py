for i in range(2, 10):
    flag = False
    for j in range(2, i):
        if i % j == 0:
            flag = True
            break

    if not flag:
        print(i)
