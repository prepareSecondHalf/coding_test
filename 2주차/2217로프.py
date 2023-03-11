import sys

n = int(sys.stdin.readline())
weight = []
for i in range(n):
    weight.append(int(sys.stdin.readline()))

weight.sort(reverse=True)
result = []
for j in range(n):
    result.append(weight[j]*(j+1))

print(max(result))