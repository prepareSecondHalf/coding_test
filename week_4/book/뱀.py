# arr[x][y]케이스
# 0 : 아무것도 없음
# 1 : 뱀이 자리함
# 2 : 사과가 자리함
# 틀렸는데 더 놀기는 눈치보임
import sys
from collections import deque

N = int(sys.stdin.readline())
K = int(sys.stdin.readline())

arr = [[0] * N for _ in range(N)]

for i in range(K):
    x, y = map(int, sys.stdin.readline().strip().split())
    arr[x][y] = 2

L = int(sys.stdin.readline())

change_dir_list = deque([])
for i in range(L):
    time, dir = sys.stdin.readline().strip().split()
    change_dir_list.append((int(time), dir))

snakes = deque([(0, 0)])
time, x, y = 0, 0, 0
dir = 1
arr[0][0] = 1

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

while True:
    time += 1
    
    nx = x + dx[dir]
    ny = y + dy[dir]

    if nx < 0 or ny < 0 or nx >= N or ny >= N or arr[nx][ny] == 1:
        print(time)
        break

    x, y = nx, ny
    snakes.append((x, y))
    arr[x][y] = 1

    if arr[x][y] == 0:
        tail = snakes.popleft()
        arr[tail[0]][tail[1]] = 0

    if len(change_dir_list) > 0 and change_dir_list[0][0] == time:
        change_dir = change_dir_list[0][1]
        change_dir_list.popleft()

        if change_dir == 'D':
            dir += 1

            if dir > 3:
                dir = 0
        else:
            dir -= 1

            if dir < 0:
                dir = 3
