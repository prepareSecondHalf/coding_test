import sys

n = int(sys.stdin.readline())
weight = []

for i in range(n):
    w = int(sys.stdin.readline())
    weight.append(w)

weight.sort(reverse=True)
result = []
maxNum = 0

for i in range(n):
    result.append(int(weight[i])*(i+1))
    
maxNum = max(result)
print(maxNum)