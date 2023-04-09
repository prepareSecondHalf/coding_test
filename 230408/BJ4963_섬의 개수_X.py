# 정사각형으로 이루어져 있는 섬과 바다 지도가 주어진다. 섬의 개수를 세는 프로그램을 작성하시오.
# 한 정사각형과 가로, 세로 또는 대각선으로 연결되어 있는 사각형은 걸어갈 수 있는 사각형이다. 
# 두 정사각형이 같은 섬에 있으려면, 한 정사각형에서 다른 정사각형으로 걸어서 갈 수 있는 경로가 있어야 한다. 
# 지도는 바다로 둘러싸여 있으며, 지도 밖으로 나갈 수 없다.

# 입력은 여러 개의 테스트 케이스로 이루어져 있다. 각 테스트 케이스의 첫째 줄에는 지도의 너비 w와 높이 h가 주어진다. w와 h는 50보다 작거나 같은 양의 정수이다.
# 둘째 줄부터 h개 줄에는 지도가 주어진다. 1은 땅, 0은 바다이다.
# 입력의 마지막 줄에는 0이 두 개 주어진다.

# 각 테스트 케이스에 대해서, 섬의 개수를 출력한다.

import sys
# 한 섬에서 다음 섬으로 넘어가기 전에 섬의 모든 땅을 탐색하므로 깊이 우선 탐색

def dfs(x, y):
    # 섬을 벗어나면 False
    if x < 0 or x >= h or y < 0 or y >= w:
        return False
    if map_data[x][y] == 1:
        map_data[x][y] = 0 # 지나간 곳을 0으로 변환
        # 주어진 위치 x, y의 상하좌우 대각선을 모두 재귀하여 탐색
        # 탐색 시, 거기서 다시 이동할 수 있는 곳이 있다면 이어서 탐색을 계속함(깊이 우선)
        dfs(x-1, y-1)
        dfs(x-1, y)
        dfs(x-1, y+1)
        dfs(x, y-1)
        dfs(x, y+1)
        dfs(x+1, y-1)
        dfs(x+1, y)
        dfs(x+1, y+1)
        # 지나간 곳은 이미 0으로 변환되었으므로, 더 이상 이동할 수 없으면 주변 및 현 위치가 모두 0이 됨 => True
        return True
    return False

while True:
    # input
    w, h = map(int, sys.stdin.readline().split())
    if w == 0 and h == 0:
        break
    map_data = []
    for i in range(h):
        map_data.append(list(map(int, sys.stdin.readline().split())))

    # w, h 탐색
    count = 0
    for i in range(h):
        for j in range(w):
            if dfs(i, j) == True:
                count += 1
    print(count)