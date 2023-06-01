# n: 수열의 크기
# 수열 a
# 출력: 수가 커지는 부분의 개수
import sys

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
dp = [1 for _ in range(n)]

for i in range(n):
    for j in range(i):
        if a[i] > a[j]:
            dp[i] = max(dp[i], dp[j] + 1)
            # ex) a = 10 20 10 30 20 50 -> dp = [1, 2, 1, 3, 2, 4]

print(max(dp))
