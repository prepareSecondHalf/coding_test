# m: 상자 가로, n: 상자 세로
# 익은 토마토: 1, 익지않은토마토: 0, 토마토가 있지않은경우: -1
from collections import deque

m, n = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]
queue = deque([])
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
count = 0

# 처음에 받은 토마토 좌표 queue에 append
for i in range(n):
    for j in range(m):
        if matrix[i][j] == 1:
            queue.append([i, j])

def bfs():
    while queue:
        x, y = queue.popleft() # 첫 토마토 x좌표 제거
        # 상하좌우 익힐 토마토 확인
        for i in range(4):
            nx, ny = dx[i] + x, dy[i] + y
            # 범위안의 토마토 and 익지않은 토마토
            if 0 <= nx < n and 0 <= ny < m and matrix[nx][ny] == 0:
                matrix[nx][ny] = matrix[x][y] + 1
                queue.append([nx, ny])

bfs()
for i in matrix:
    for j in i:
        # 다 익히지 못하는 상황일때
        if j == 0:
            print(-1)
            exit(0)
    count = max(count, max(i))
print(count - 1)