# 화성은 에너지 공급원을 찾기 힘들다.
# 효율적으로 에너지를 사용하려면 출발 지점에서 목표 지점까지 항상 최단 경로를 찾아야 한다.
# 기계가 존재하는 공간은 N X N의 2차원 공간이며, 각 칸을 지나기 위한 비용이 존재한다.
# 가장 왼쪽 위 칸인 [0][0]에서 가장 오른쪽 아래인 [N-1][N-1]로 이동하는 최소 비용을 출력하는 프로그램을 작성하시오.
# 탐사 기계는 특정 위치에서 상하좌우 인접한 곳으로 1칸만 이동 가능하다.

# 입력
# 첫째 줄에 테스트 케이스의 수 T가 주어진다. (1 <= T <= 10)
# 테스트 케이스의 첫째 줄에는 탐사 공간의 크기 N(2 <= N <= 125)이 주어진다.
# N개의 줄에 각 칸의 비용이 공백으로 구분되어 주어진다. (0 <= 비용 <= 9)

# 출력
# 각 케이스마다 최소 비용을 한 줄에 하나씩 출력한다.

import sys
import heapq

t = int(sys.stdin.readline())
# 풀이
# 한 지점(1)에서 목적지까지 가는 최단 경로이므로 다익스트라
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
INF = float("inf")
for _ in range(t):
    n = int(sys.stdin.readline())
    graph = []
    for i in range(n):
        graph.append(list(map(int, sys.stdin.readline().split())))

    # 최단 거리 table
    INF
    distances = [[INF] * n for _ in range(n)]

    # 0, 0 start
    x, y = 0, 0
    q = [(graph[x][y], x, y)]
    distances[x][y] = graph[x][y]

    while q:
        dist, x, y = heapq.heappop(q)
        if distances[x][y] < dist:
            # 처리된 경우 무시
            continue
        for i in range(4):
            # 각 방향 체크
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                # 그래프 범위 벗어나면 무시
                continue
            cost = dist + graph[nx][ny]
            if cost < distances[nx][ny]:
                distances[nx][ny] = cost
                heapq.heappush(q, (cost, nx, ny))

print(distances[n - 1][n - 1])
