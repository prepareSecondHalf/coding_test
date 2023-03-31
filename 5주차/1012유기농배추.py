# t: 테스트케이스의 수
# m: 가로, n: 세로, k: 배추의 개수
# x: 배추의 위치
from collections import deque

#방향
dx = [0,0,1,-1]
dy = [1,-1,0,0]

t = int(input())

def bfs(graph, a, b):
    queue = deque()
    queue.append((a,b))
    graph[a][b] = 0

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx < 0 or nx >=n or ny < 0 or ny >= m: #좌표가 범위 밖일때
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                queue.append((nx, ny))
    return

for i in range(t):
    cnt = 0
    n, m, k = map(int,input().split())
    graph = [[0]*m for _ in range(n)]

    for j in range(k):
        x, y = map(int, input().split())
        graph[x][y] = 1

    for a in range(n):
        for b in range(m):
            # 배추가 있는칸일때 bfs 실행, cnt 1증가
            if graph[a][b] == 1:
                bfs(graph, a, b)
                cnt += 1
    print(cnt)