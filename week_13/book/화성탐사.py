# 뭐여 이게 다익스트라 아니여?
# 못품
import sys
import heapq

INF = int(1e9)

dx = [0,1,0,-1]
dy = [1,0,-1,0]

t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())
    graph = []

    for i in range(n):
        graph.append(list(map(int, sys.stdin.readline().strip().split())))

    distance = [[INF] * n for _ in range(n)]

    x, y = 0, 0
    q = [(graph[x][y], x, y)]
    distance[x][y] = graph[x][y]

    while q:
        dist, x, y = heapq.heappop(q)

        if distance[x][y] < dist:
            continue

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue

            cost = dist + graph[nx][ny]

            if cost < distance[nx][ny]:
                 distance[nx][ny] = cost
                 heapq.heappush(q, (cost, nx, ny))
    
    print(distance[n - 1][n - 1])