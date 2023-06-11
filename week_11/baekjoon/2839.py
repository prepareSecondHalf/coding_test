import sys

N = int(sys.stdin.readline())

result = 0

while True:
    if N % 5 == 0:
        result += N // 5
        break
    
    N -= 3

    if N < 0:
        result = -1
        break
    
    result += 1

print(result)