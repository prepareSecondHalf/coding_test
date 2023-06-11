import heapq
import sys

INF = int(1e9)

N, M, start = map(int, sys.stdin.readline().strip().split())

graph = [[] for i in range(N + 1)]
distance = [INF] * (N + 1)

for _ in range(M):
    a, b, c = map(int, sys.stdin.readline().strip().split())
    graph[a].append((b, c))

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

dijkstra(start)

nodeCnt = 0
time = 0

for i in range(1, N + 1):
    if distance[i] != INF:
        nodeCnt += 1
        # 아 이것도 아니네 ㅋㅋ
        # 시간을 다 더하는게 아니라 그냥 제일 긴 애만 찾으면 되는거잖아
        # time += distance[i]
        time = max(time, distance[i])

# 아 자기 자신 하나 빼라고...
print(nodeCnt - 1, time)