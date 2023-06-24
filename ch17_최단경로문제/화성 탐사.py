'''
    출발에서 목표까지 이동 시, 항상 최적 경로 찾도록 개발
    n x n크기의 2차원 공간
    [0][0]에서 [n - 1] 로 이동하는 최소 비용 출력
    상하좌우 인접한 곳 이동 가능
'''

import sys
import heapq
INF = int(1e9)
input = sys.stdin.readline

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

t = int(input())

for _ in range(t):
    n = int(input())
    graph = []

    for i in range(n):
        graph.append(list(map(int, input().split())))
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

            if nx < 0 or nx >= n or ny < 0 or ny > n:
                continue
            cost = dist + graph[nx][ny]
            if cost < distance[nx][ny]:
                distance[nx][ny] = cost
                heapq.heappush(q, (cost, nx, ny))

    print(distance[n - 1][n - 1])

    