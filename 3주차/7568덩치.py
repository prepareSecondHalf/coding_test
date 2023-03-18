import sys

n = int(sys.stdin.readline())
spec = []

for i in range(n):
    spec.append(list(map(int, sys.stdin.readline().split())))

for j in range(n):
    rank = 1
    for k in range(n):
        if spec[j][0] < spec[k][0] and spec[j][1] < spec[k][1]:
            rank += 1
    print(rank, end=' ')