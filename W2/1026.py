import sys

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
b = list(map(int, sys.stdin.readline().split()))

tempA = a
tempA.sort(reverse=True)
tempB = b
tempB.sort()

sum = 0;

for i in range(n):
  sum += tempA[i] * tempB[i]

print(sum)