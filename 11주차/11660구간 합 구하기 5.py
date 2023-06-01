# n: 표의 가로세로길이 m: 합을 구해야 하는 횟수
import sys

n, m = map(int, sys.stdin.readline().split())
line_n = []
line_m = []
dp = [[0] * (n+1) for _ in range(n+1)]
for _ in range(n):
    line_n.append(list(map(int, sys.stdin.readline().split())))

# dp에 [0][0] 부터 해당 좌표까지의 합들을 넣어준다
# ex) line_n = [[1 2], [3 4]] 일때 dp = [[0, 0, 0], [0, 1, 3], [0, 4, 11]] (아래처럼 for문을 돌릴때 indexError방지를 위해 첫줄은 0으로 채운다)
# 0 0 0
# 0 1 3
# 0 4 11
for i in range(1, n+1):
    for j in range(1, n+1):
        # 가장왼쪽위 좌표부터 해당좌표까지의 합들을 넣어줌 
        # 좌표기준 왼쪽 좌표까지의 합 + 위쪽까지의 합 + 현재 좌표값 - 왼쪽과 위쪽좌표를 합했을때 겹쳐서 더해진값
        dp[i][j] = dp[i-1][j] + dp[i][j-1] + line_n[i-1][j-1] - dp[i-1][j-1]

for i in range(m):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    # [x2][y2]좌표까지의 합 - 범위에 들어오지않는 상단부분 - 범위에 들어오지않는 좌측부분 + 겹쳐서 두번빼진부분
    print(dp[x2][y2] - dp[x1-1][y2] - dp[x2][y1-1] + dp[x1-1][y1-1])



# 오답
# for _ in range(m):
#     line_m.append(list(map(int, sys.stdin.readline().split())))

# for i in range(m):
#     x1, y1 = line_m[i][0], line_m[i][1]
#     x2, y2 = line_m[i][2], line_m[i][3]
#     result = 0
#     while x1 <= x2 and y1 <= y2:
#          result += line_n[x1-1][y1-1]
#          if x1 < x2:
#              x1 += 1
#          else:
#             y1 += 1
#     print(result)


