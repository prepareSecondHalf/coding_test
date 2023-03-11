import sys

n, m = map(int, sys.stdin.readline().split())
data = list(map(int, sys.stdin.readline().split()))

array = [0] * 11

for i in data:
    array[i] +=1
result = 0
for j in range(1, m+1):
    n -= array[i]
    result += array[i] * n
print(result)