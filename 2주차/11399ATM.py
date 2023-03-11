import sys

n = int(sys.stdin.readline())
s = list(map(int, sys.stdin.readline().split()))
num = 0
s.sort()
for i in range(n):
    for j in range(i + 1):
        num += s[j]
print(num)