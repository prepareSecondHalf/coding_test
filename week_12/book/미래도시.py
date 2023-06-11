# 다익스트라로 1 -> K 의 거리 최소
# K -> X 의 거리 최소 구해서 더한다?
import sys
import heapq

INF = int(1e9)

N, M = map(int, sys.stdin.readline().strip().split())
graph = [[] for i in range(N + 1)]
distance = [INF] * (N + 1)

for _ in range(M):
    a, b = map(int, sys.stdin.readline().strip().split())
    graph[a].append((b, 1))
    graph[b].append((a, 1))

X, K = map(int, sys.stdin.readline().strip().split())

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(1)
oneToK = distance[K]

distance = [INF] * (N + 1)
dijkstra(K)
KToX = distance[X]

if oneToK == INF or KToX == INF:
    print(-1)
else:
    print(oneToK + KToX)