#     7
#    3 8
#   8 1 0
#  2 7 4 4
# 4 5 2 6 5
# 위 그림은 크기가 5인 정수 삼각형이다. 맨 위층부터 시작해서 아래층 수 중 하나를 선택해서 내려올 때, 선택된 수들의 합의 최댓값을 구하라.
# 현재 층에서 대각선 왼쪽 또는 대각선 아래쪽만 선택 가능하다.
# 삼각형의 크기는 1~500이며, 삼각형을 이루는 모든 수는 0~9999의 정수이다.

# 첫째 줄에 삼각형의 크기 n, 둘째 줄부터 n+1번째 줄까지 정수 삼각형이 주어진다.
# 첫째 줄에 합의 최댓값을 출력한다.

# 5
# 7
# 3 8
# 8 1 0
# 2 7 4 4
# 4 5 2 6 5

import sys
n = int(sys.stdin.readline())
triangles = []
for i in range(n):
    integer = list(map(int, sys.stdin.readline().split()))
    triangles.append(integer)
# print(*triangles, sep='\n')

# 풀이: 정수 3개짜리 삼각형이 반복되어 있다고 생각하면 된다.
#     7
#    3 8
#   8 1 0
#  2 7 4 4
# 4 5 2 6 5
# 이렇게 주어진 삼각형을
#          7
#       10  15
#     18  16  15
#   20  25  20  19
# 24  30  27  26  24
# 이런 dp table로 만들어서 마지막 line의 최댓값을 구하는 것...


dp = [[0] * n for _ in range(n)]
dp[0][0] = triangles[0][0]
dp[1][0] = dp[0][0] + triangles[1][0]
dp[1][1] = dp[0][0] + triangles[1][1]
# print('-----init dp table-----')
# print(*dp, sep='\n')

for i in range(2, n):
    for j in range(0, i+1):
        dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + triangles[i][j]

# print('-----dp table-----')
# print(*dp, sep='\n')
print(max(dp[n-1]))