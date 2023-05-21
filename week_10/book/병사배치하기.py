# 이거일 리가 없지
import sys

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().strip().split()))

result = 0

for i in range(N):
    if i < N - 1:
        if arr[i] < arr[i + 1]:
            result += 1

print(result)

# 정답
N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().strip().split()))
arr.reverse()

dp = [1] * N

# 이게 가장 긴 증가하는 부분 수열 문제 과정인듯
# 0 <= j < i 에 대해 D[i] = max(D[i], D[j] + 1) if array[j] < array[i] 가 공식이라고 했으니까
# 걍 외우는걸로
for i in range(1, N):
    for j in range(0, i):
        if arr[j] < arr[i]:
            dp[i] = max(dp[i], dp[j] + 1)

print(N - max(dp)) # 열외시켜야 되는거니까 N에서 최대길이 구한걸 빼는거고..