# n: 계단의 개수
# n개의 계단당 점수
# 문제
# 1. 계단은 한 번에 한 계단씩 또는 두 계단씩 오를 수 있다. 즉, 한 계단을 밟으면서 이어서 다음 계단이나, 다음 다음 계단으로 오를 수 있다.
# 2. 연속된 세 개의 계단을 모두 밟아서는 안 된다. 단, 시작점은 계단에 포함되지 않는다. (3번연속 1계단 이동불가)
# 3. 마지막 도착 계단은 반드시 밟아야 한다.
# 출력: 계단오르기 게임에서 얻을수 있는 점수의 최댓값
import sys

n = int(sys.stdin.readline())
point = [0 for i in range(301)]
dp = [0 for i in range(301)]
# point = []
# dp = [0] * n
for i in range(n):
    point[i] = int(sys.stdin.readline())
    # point.append(int(sys.stdin.readline()))


dp[0] = point[0]
dp[1] = point[0] + point[1]
dp[2] = max(point[0] + point[2], point[1] + point[2])

for i in range(3, n):
    dp[i] = max(dp[i - 2] + point[i], dp[i-3] + point[i-1] + point[i])
print(dp[n-1])
# 질문: point와 dp를 주석해놓은 형태로 바꾼후 append로 넣어서 채점을 돌리면 indexError가 나오는데 테스트할때는 답이 맞게 나오는거같은데
# 어느부분에서 indexError가 나오는지 이해가 가지않는다