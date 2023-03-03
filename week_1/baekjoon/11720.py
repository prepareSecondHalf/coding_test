import sys

N = int(sys.stdin.readline())
num = int(sys.stdin.readline())

sum = 0

for i in str(num):
    sum += int(i)
    
print(sum)