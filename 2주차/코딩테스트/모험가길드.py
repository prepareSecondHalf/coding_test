import sys

n = int(sys.stdin.readline())
data = list(map(int, sys.stdin.readline().split()))
data.sort()

result = 0
count = 0

for i in range(n):
    count +=1
    if count >=i:
        result +=1
        count = 0
print(result)
