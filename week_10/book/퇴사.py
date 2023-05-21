# 못품
# 이해도 안됨
import sys

N = int(sys.stdin.readline())

t = []
p = []
dp = [0] + (N + 1)
max_value = 0

for _ in range(N):
    x, y = map(int, sys.stdin.readline().strip().split())
    t.append(x)
    p.append(y)

for i in range(N - 1, -1, -1):
    time = t[i] + i # 이해 안됨

    if time <= N:
        dp[i] = max(p[i] + dp[time], max_value)
        max_value = dp[i]
    else:
        dp[i] = max_value

print(max_value)