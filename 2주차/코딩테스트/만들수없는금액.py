import sys

n = int(sys.stdin.readline())
data = list(map(int, sys.stdin.readline().split()))
data.sort()

target = 1
for i in data:
    if target < x:
        break
    target += i
print(target)