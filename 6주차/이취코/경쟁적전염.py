# 백준 18405
# N: 가로 세로 , K: 바이러스의 종류
# 시험관의 정보, 존재하는 바이러스의 번호
# 마지막줄에는 S,X,Y
# 출력: S초 뒤 (X,Y에 존재하는 바이러스의 종류
# 1초마다 상하좌우로 번호가 낮은 바이러스부터 증식 이미 바이러스가 들어간 칸은 다른바이러스 증식 불가
from collections import deque

N, K = map(int, input().split())
graph = []
virus = []
for i in range(N):
    graph.append(list(map(int, input().split())))
    for j in range(N):
        # 바이러스가 존재할경우 virus에 바이러스번호와 좌표를 append
        if graph[i][j] != 0:
            virus.append(((graph[i][j], i, j)))
S, X, Y = map(int, input().split())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(s, X, Y):
    q = deque(virus)
    count = 0
    while q:
        if count == s:
            break
        for _ in range(len(q)):
            prev, x, y = q.popleft() # 바이러스번호, X좌표, Y 좌표
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < N and 0 <= ny < N:
                    # 이동한 좌표에 바이러스가 없을시 이동하기전 좌표의 바이러스번호로 변경, q에 바이러스번호와 좌표를 저장
                    if graph[nx][ny] == 0:
                        graph[nx][ny] = graph[x][y]
                        q.append((graph[nx][ny], nx, ny))
        count += 1
    return graph[X - 1][Y - 1]


virus.sort()
print(bfs(S, X, Y))