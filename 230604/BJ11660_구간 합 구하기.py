# N×N개의 수가 N×N 크기의 표에 채워져 있다.
# (x1, y1)부터 (x2, y2)까지 합을 구하는 프로그램을 작성하시오. (x, y)는 x행 y열을 의미한다.

# 예를 들어, N = 4이고, 표가 아래와 같이 채워져 있는 경우를 살펴보자.
# 1	2	3	4
# 2	3	4	5
# 3	4	5	6
# 4	5	6	7
# 여기서 (2, 2)부터 (3, 4)까지 합을 구하면 3+4+5+4+5+6 = 27이고, (4, 4)부터 (4, 4)까지 합을 구하면 7이다.

# 표에 채워져 있는 수와 합을 구하는 연산이 주어졌을 때, 이를 처리하는 프로그램을 작성하시오.

import sys

n, m = map(int, sys.stdin.readline().split())
table = []
for i in range(n):
    row = list(map(int, sys.stdin.readline().split()))
    table.append(row)
# print("-----------------------")
# print(*table, sep="\n")
# print("-----------------------")
# 풀이: 구간의 합을 2차원 dp table에 저장하면 된다
# 1	2	3	4
# 2	3	4	5
# 3	4	5	6
# 4	5	6	7
# 이렇게 있다면, dp[i][i]는 왼쪽에 저장된 값과 위에 저장된 값인 dp[i-1][i], dp[i][i-1]
# 그리고 해당 위치의 값 table[i][i]을 더한 뒤, 위에서 중복된 값인 dp[i-1][i-1]을 빼면 된다.
# 1   3   6   10
# 3   8   15  24
# 6   15  27  42
# 10  24  42  64

dp = [[0] * n for _ in range(n)]
dp[0][0] = table[0][0]
for i in range(n):
    for j in range(n):
        if i - 1 < 0:
            dp[i][j] = dp[i][j - 1] + table[i][j]
        elif j - 1 < 0:
            dp[i][j] = dp[i - 1][j] + table[i][j]
        else:
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1] + table[i][j] - dp[i - 1][j - 1]
# print(*dp, sep="\n")

# 테이블을 만들었으면 부분합을 구하면 된다.
# dp[y2-1][x2-1]는 (1, 1)부터 (x2, y2)까지의 부분합이다.
# (1, y1), (x1, 1)까지의 부분합은 필요없으므로
# dp[y1-1][0]과 dp[0][x1-1]까지는 빼 준다.
# 이렇게 하면 dp[y1-2][x1-2]이 두 번 빠졌으므로 한 번 더해 준다.

for i in range(m):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    if x1 == x2 and y1 == y2:
        print(table[x1 - 1][y1 - 1])
    elif x1 - 2 < 0 or y1 - 2 < 0:
        print(dp[y2 - 1][x2 - 1])
    else:
        print(
            dp[y2 - 1][x2 - 1]
            - dp[y2 - 1][x1 - 2]
            - dp[y1 - 2][x2 - 1]
            + dp[y1 - 2][x1 - 2]
        )
