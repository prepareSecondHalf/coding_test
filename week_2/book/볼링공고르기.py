import sys

# 내가 생각한 코드
N, M = map(int, sys.stdin.readline().strip().split())
data = list(map(int, sys.stdin.readline().strip().split()))

cnt = 0

for i in range(N - 1):
    for j in range(i + 1, N):
        if data[i] != data[j]:
            cnt += 1
            
print(cnt)

# 답
N, M = map(int, sys.stdin.readline().strip().split())
data = list(map(int, sys.stdin.readline().strip().split()))

arr = [0] * 11

for x in data:
	arr[x] += 1

result = 0

for i in range(1, M + 1):
	N -= arr[i]
	result += arr[i] * N