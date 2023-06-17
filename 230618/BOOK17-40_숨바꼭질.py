# 1~N까지의 헛간 중 하나를 골라 숨을 수 있다.
# 술래는 항상 1에서 출발한다.
# 전체 맵에는 M개의 양방향 통로가 존재한다.
# 1번에서 최단 거리가 가장 먼 헛간이 안전하다고 판단하여 거기에 숨으려 한다.
# 숨을 헛간의 번호를 출력하시오.

# 입력
# 첫째 줄에는 N(2 <= N <= 20000), M(1 <= ㅡ <= 50000)이 공백으로 구분되어 주어진다.
# 이후 M개의 줄에 걸쳐 A, B의 번호가 공백으로 구분되어 주어진다.

# 출력
# 숨어야 하는 헛간 번호, 헛간까지의 거리, 같은 거리에 있는 헛간의 개수를 띄어쓰기로 구분하여 출력한다.


import sys
import heapq

n, m = map(int, sys.stdin.readline().split())
# 풀이
start = 1  # 출발점
graph = [[] for _ in range(n + 1)]
INF = float("inf")
distance = [INF] * (n + 1)
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    # 양방향이므로 비용을 1로 하여 graph 초기화
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


dijkstra(start)

max_node = 0  # 숨을 곳
max_distance = 0  # 까지의 거리
maxes = []  # 동일한 거리 리스트

for i in range(1, n + 1):
    if max_distance < distance[i]:
        max_node = i
        max_distance = distance[i]
        maxes = [max_node]
    elif max_distance == distance[i]:
        maxes.append(i)
print(max_node, max_distance, len(maxes))
