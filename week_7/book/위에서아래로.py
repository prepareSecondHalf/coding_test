import sys

N = int(sys.stdin.readline())

arr = []
for _ in range(N):
	arr.append(int(sys.stdin.readline()))

arr.sort(reverse=True)

for data in arr:
	print(data, end=' ')