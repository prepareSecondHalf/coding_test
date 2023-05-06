import sys

N = int(sys.stdin.readline())

homes = list(map(int, sys.stdin.readline().strip().split()))
homes.sort()

mid = 0

if N % 2 == 0:
	idx = N // 2
	mid = (homes[idx - 1] + homes[idx]) / 2

	if abs(homes[idx - 1] - mid) > abs(homes[idx] - mid):
		mid = homes[idx]
	else:
		mid = homes[idx - 1]
else:
	idx = N // 2
	mid = homes[idx]

print(mid)