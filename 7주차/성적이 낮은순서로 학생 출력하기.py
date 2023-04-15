import sys

n = int(sys.stdin.readline())
point = []

for _ in range(n):
    data = sys.stdin.readline().split()
    point.append((data[0], int(data[1])))

point.sort(key=lambda a: a[1])

for i in range(n):
    print(point[i][0], end=" ")