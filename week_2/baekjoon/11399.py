import sys

N = int(sys.stdin.readline())
data = list(map(int, sys.stdin.readline().strip().split()))

data.sort()

result = 0

for i in range(0, N + 1):
    result += sum(data[:i])
    
print(result)