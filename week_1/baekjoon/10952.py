import sys

while True:
    n, m = map(int, sys.stdin.readline().strip().split())
    
    if n == 0 and m == 0:
        break
    else:
        print(n + m)