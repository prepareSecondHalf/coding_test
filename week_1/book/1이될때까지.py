import sys

n, k = map(int, sys.stdin.readline().strip().split())

result = 0

while n != 1:
	if n % k != 0:
		n -= 1
		result += 1

	else:
		n //= k
		result += 1

print(result)