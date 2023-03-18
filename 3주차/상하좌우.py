import sys

n = int(sys.stdin.readline())
move = sys.stdin.readline().split()
a = [1, 1]

for i in move:
    if i == 'U':
        if a[0] == 1:
            pass
        elif a[0] < n:
            a[0] += 1
    elif i == 'D':
        if a[0] == n:
            pass
        elif a[0] < n:
            a[0] += 1

    elif i == 'R':
        if a[1] == n:
            pass
        elif a[1] < n:
            a[1] += 1
    else:
        if a[1] == 1:
            pass
        elif a[1] < n:
            a[1] += 1
print(a[0], a[1])