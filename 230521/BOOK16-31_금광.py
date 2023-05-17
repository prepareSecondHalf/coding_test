# n x m 크기의 금광이 있다. 이는 1x1의 칸으로 나누어져 있고, 각 칸은 특정 크기의 금이 있다.
# 채굴자는 첫 번째 열부터 출발해서 금을 캔다.
# 맨 처음에는 첫 열의 어느 행에서든 출발이 가능하고 
# 이후 m번에 걸쳐 오른쪽 위, 오른쪽, 오른쪽 아래 중 하나로 이동한다.
# 이동하면서 얻을 수 있는 최대 금의 크기를 구하는 프로그램을 작성하시오

# 첫째 줄에 테스트 케이스 T가 입력된다. (1 <= T <= 1000)
# 각 테스트 케이스 첫째 줄에 n과 m이 공백으로 구분되어 입력된다. (1 <= n, m <= 20)
# 둘째 줄에 n x m개의 위치에 매장된 금의 개수가 공백으로 구분되어 입력된다. (1 <= 금의 개수 <= 100)

# 테스트 케이스마다 얻을 수 있는 최대 금의 크기를 줄을 바꿔 구분하여 출력한다. 

import sys

for t in range(int(sys.stdin.readline().strip())):
    n, m = map(int, sys.stdin.readline().split())
    array = list(map(int, sys.stdin.readline().split()))

    # 2차원 dp table 초기화
    dp = []
    index = 0
    for i in range(n):
        dp.append(array[index:index+m])
        index += m

    print(dp)
    for j in range(1, m):
        for i in range(n):
            if i == 0: # 왼쪽 위
                from_left_up = 0
            else:
                from_left_up = dp[i-1][j-1]
            
            if i == n-1: # 왼쪽 아래
                from_left_down = 0
            else:
                from_left_down = dp[i+1][j-1]
            
            left = dp[i][j-1]

            dp[i][j] = dp[i][j] + max(from_left_up, from_left_down, left)

    result = 0
    for i in range(n):
        result = max(result, dp[i][m-1])
    print(result)

# 테스트 케이스
# 2
# 3 4
# 1 3 3 2 2 1 4 1 0 6 4 7
# 4 4
# 1 3 1 5 2 2 4 1 5 0 2 3 0 6 1 2