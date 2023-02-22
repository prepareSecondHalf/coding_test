import sys

N = list(map(int, sys.stdin.readline().strip().split()))

sum = 0

for data in N:
    sum += data ** 2

print(sum % 10)