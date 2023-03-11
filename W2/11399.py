import sys

n = int(sys.stdin.readline())
list = list(map(int, sys.stdin.readline().split()))

list.sort()
res = 0

for i in range(n):
  for j in range(i+1):
    res += list[j]

print(res)