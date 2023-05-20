# n: 남은 근무일수
# t: 상담완료까지 걸리는 일수 p: 금액
# 문제: 1일부터 n일까지의 상담일정 각 일정마다 t일이 소요되며 완료시 p를 수당으로 받는다
# 출력: 최대수익
import sys

n = int(sys.stdin.readline())
schedule = []
dp = [0] * (n+1)
for _ in range(n):
    schedule.append(list(map(int, sys.stdin.readline().split())))

# n일부터 1일까지
for day in range(n-1, -1, -1):
    t, p = schedule[day]
    # 현재일 + 걸리는일수 > 근무일수일때 다음날 금액을 삽입
    if day + t > n:
        dp[day] = dp[day+1]
    # 현재일 + 걸리는일수 < 근무일수일때 다음날 금액, 현재건의 금액 + t일뒤 금액중 큰값을 삽입
    else:
        dp[day] = max(dp[day+1], p+dp[day+t])
print(dp[0])
