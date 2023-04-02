'''
    가로 m
    세로 n
    n개의 줄에는 상자에 담긴 토마토의 정보
    m개의 토마토 상태 (0 = 익지 않음, 1 = 익음, -1 = 토마토가 없음)

    모두 익을 때까지의 최소 날짜
    저장될 때부터, 모든 토마토 익는 상태 = 0
    익지 못 하는 상태 = -1
'''

import sys
from collections import deque
input = sys.stdin.readline

m, n = map(int, input().split())
box = [] # 토마토 상태 저장하는 2차원 리스트
tomato = [] # 익은 토마토 위치 저장 리스트
for i in range(n):
    box.append(list(map(int, input().split())))
    for j in range(m):
        if box[i][j] == 1:
            tomato.append((0, i, j))

q = deque(tomato)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

while q:
    day, x, y = q.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        # 이동위치에 덜 익은 토마토 있으면 익은 상태로 바꿔준다(0 -> 1)
        if 0 <= nx < n and 0 <= ny < m and box[nx][ny] == 0:
            box[nx][ny] = 1
            q.append((day + 1, nx, ny))


# 토마토가 모두 익지 못하는 경우, -1 출력 후 종료
for i in range(n):
    if 0 in box[i]:
        print(-1)
        sys.exit(0)

print(day)

