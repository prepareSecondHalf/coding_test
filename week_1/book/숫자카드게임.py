import sys

# 내가 생각한 코드
n, m = map(int, sys.stdin.readline().strip().split())

result = []

for i in range(n):
	data = list(map(int, sys.stdin.readline().strip().split()))
	result.append(min(data))

print(max(result))


# 정답 코드
n, m = map(int, sys.stdin.readline().strip().split())

result = 0

for i in range(n):
	data = list(map(int, sys.stdin.readline().strip().split()))
	min_value = min(data)
	result = max(result, min_value)

print(result)