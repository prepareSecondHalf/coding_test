import sys

n, target = map(int, sys.stdin.readline().strip().split())
num_list = list(map(int, sys.stdin.readline().strip().split()))

for i in range(n):
    if num_list[i] < target:
        print(num_list[i], end=' ')