# 고등학교 수열때나 배우던 문제
# Sum[i] = A[0] + A[1] + ... + A[i]라고 했을 때
# Sum[i] = S[i - 1] + A[i] 로 표현할 수 있다는... 아주 옛날 이야기..

import sys

N, M = map(int, sys.stdin.readline().strip().split())

arr = []
for i in range(N):
    arr.append(list(map(int, sys.stdin.readline().strip().split())))

dp = [[0] * (N + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    for j in range(1, N + 1):
        dp[i][j] = dp[i][j - 1] + dp[i - 1][j] - dp[i - 1][j - 1] + arr[i][j]

for k in range(M):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().strip().split())

    result = dp[x2][y2] - dp[x2][y1 - 1] - dp[x1 - 1][y2] + dp[x1 - 1][y1 - 1]
    print(result)