# RGB거리에는 집이 N개 있다. 거리는 선분으로 나타낼 수 있고, 1번 집부터 N번 집이 순서대로 있다.
# 집은 빨강, 초록, 파랑 중 하나의 색으로 칠해야 한다. 
# 각각의 집을 빨강, 초록, 파랑으로 칠하는 비용이 주어졌을 때, 아래 규칙을 만족하면서 모든 집을 칠하는 비용의 최솟값을 구해보자.

# 1번 집의 색은 2번 집의 색과 같지 않아야 한다.
# N번 집의 색은 N-1번 집의 색과 같지 않아야 한다.
# i(2 ≤ i ≤ N-1)번 집의 색은 i-1번, i+1번 집의 색과 같지 않아야 한다.

# 첫째 줄에 집의 수 N(2 ≤ N ≤ 1,000)이 주어진다. 
# 둘째 줄부터 N개의 줄에는 각 집을 빨강, 초록, 파랑으로 칠하는 비용이 1번 집부터 한 줄에 하나씩 주어진다. 
# 집을 칠하는 비용은 1,000보다 작거나 같은 자연수이다.

# 첫째 줄에 모든 집을 칠하는 비용의 최솟값을 출력한다.

import sys

n = int(sys.stdin.readline())
RGBs = []
for i in range(n):
    RGB = list(map(int, sys.stdin.readline().split()))
    RGBs.append(RGB)
# print('rgb data')
# print(*RGBs, sep='\n')

# 똑같이 생긴(3*n) 2차원 dp table을 만들어 나가면 된다
# 71 39 44
# 32 83 55
# 51 37 63
# 89 29 100
# 83 58 11
# 65 13 15
# 47 25 29
# 60 66 19
# 이런 케이스가 있다면
#    71    39     44  <=  첫 줄
# 32+39  83+44  55+39  <= 각 열은 이전 행(dp[i-1][])에서 더 작은 수를 골라 현재 위치(RGBS[i][])에 더하는 케이스를 dp table로 만들면 된다.
dp = [[0] * 3 for _ in range(n)]
dp[0] = RGBs[0]
# print('initial dp table')
# print(*dp, sep='\n')
for i in range(1, n):
    dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + RGBs[i][0]
    dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + RGBs[i][1]
    dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + RGBs[i][2]
# print('updated dp table')
# print(*dp, sep='\n')
print(min(dp[n-1]))