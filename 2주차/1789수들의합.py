import sys

s = int(sys.stdin.readline())
num = 0
result = 0
for i in range(1, s+1):
    num += i
    result += 1
    if num > s:
        result -= 1
        break

print(result)