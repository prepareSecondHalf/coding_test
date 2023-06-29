t = int(input())
for i in range(1, t + 1):
    # print(i)
    for j in range(t - i):
        print(' ', end='')
    for j in range(i):
        print('*', end='')
    print()
