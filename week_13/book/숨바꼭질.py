import sys
import heapq
input = sys.stdin.readline

INF = int(1e9)

N, M = map(int, input().split())
graph = [[] for i in range(N + 1)]
distance = [INF] * (N + 1)

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append((b, 1))
    graph[b].append((a, 1))

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

max = 0
max_distance = 0
cnt = 0

for i in range(1, N + 1):
    if max_distance < distance[i]:
        max = i
        max_distance = distance[i]
        cnt = 1
    elif max_distance == distance[i]:
        cnt += 1

print(max, max_distance, cnt)