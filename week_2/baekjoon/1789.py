import sys

S = int(sys.stdin.readline())

num = 0

while S > num:
    num += 1
    S -= num
    
print(num)