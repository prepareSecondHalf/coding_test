import sys

# 내가 생각한 답
N = int(sys.stdin.readline())
data = list(map(int, sys.stdin.readline().strip().split()))

data.sort()

target = 1

for i in data:
    if i > target:
        break
    target += i
    
print(target)