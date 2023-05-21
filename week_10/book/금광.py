# import sys

# T = int(sys.stdin.readline())

# for _ in range(T):
#     N, M = map(int, sys.stdin.readline().strip().split())
#     arrTmp = list(map(int, sys.stdin.readline().strip().split()))

#     arr = []

#     for i in range(M):
#         arr.append([arrTmp[x] for x in range(N * M) if x % M == i])

#     d = [0] * (M + 1)

#     # ? 모르겠는데요

# 답안
import sys
t = int(sys.stdin.readline())
for _ in range(t):
    n, m = map(int, sys.stdin.readline().rstrip().split())
    data = list(map(int, sys.stdin.readline().rstrip().split()))

    dp = []
    index = 0
    for _ in range(n):
        dp.append(data[index: index + m])
        index += m # n개씩 끊는게 아니라 m개씩 끊어서

    # 이전 문제들과 달리 첫번째 세팅 필요 없이 문제 풀이
    # 왼쪽 -> j - 1 / 위쪽 -> i - 1 / 아래쪽 -> i + 1
    # 아예 맨 왼쪽 데이터부터 시작하는게 아닌 그 다음 데이터들부터 시작
    for j in range(1, m):
        for i in range(n):
            if i == 0:
                left_up = 0
            else:
                left_up = dp[i - 1][j - 1]

            if i == n - 1:
                left_down = 0

            else:
                left_down = dp[i + 1][j - 1]

            left = dp[i][j - 1]
            dp[i][j] = dp[i][j] + max(left_up, left, left_down)

    result = 0
    for i in range(n):
        result = max(result, dp[i][m - 1])

    print(result)