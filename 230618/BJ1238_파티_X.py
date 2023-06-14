# N개의 숫자로 구분된 각각의 마을에 한 명의 학생이 살고 있다.

# 어느 날 이 N명의 학생이 X (1 ≤ X ≤ N)번 마을에 모여서 파티를 벌이기로 했다. 
# 이 마을 사이에는 총 M개의 단방향 도로들이 있고 i번째 길을 지나는데 Ti(1 ≤ Ti ≤ 100)의 시간을 소비한다.

# 각각의 학생들은 파티에 참석하기 위해 걸어가서 다시 그들의 마을로 돌아와야 한다. 
# 하지만 이 학생들은 워낙 게을러서 최단 시간에 오고 가기를 원한다.

# 이 도로들은 단방향이기 때문에 아마 그들이 오고 가는 길이 다를지도 모른다. 
# N명의 학생들 중 오고 가는데 가장 많은 시간을 소비하는 학생은 누구일지 구하여라.

# 입력
# 첫째 줄에 N(1 ≤ N ≤ 1,000), M(1 ≤ M ≤ 10,000), X가 공백으로 구분되어 입력된다. 
# 두 번째 줄부터 M+1번째 줄까지 i번째 도로의 시작점, 끝점, 그리고 이 도로를 지나는데 필요한 소요시간 Ti가 들어온다. 
# 시작점과 끝점이 같은 도로는 없으며, 시작점과 한 도시 A에서 다른 도시 B로 가는 도로의 개수는 최대 1개이다.
# 모든 학생들은 집에서 X에 갈수 있고, X에서 집으로 돌아올 수 있는 데이터만 입력으로 주어진다.

# 출력
# 첫 번째 줄에 N명의 학생들 중 오고 가는데 가장 오래 걸리는 학생의 소요시간을 출력한다.

import sys
n, m, x = map(int, sys.stdin.readline().split())

# 아래와 같은 케이스에서, 4명의 학생이 8개의 도로를 이용해 2번 마을에서 파티하는 것...
# n: 4   m: 8   x: 2
# s: 1   e: 2   t: 4
# s: 1   e: 3   t: 2
# s: 1   e: 4   t: 7
# s: 2   e: 1   t: 1
# s: 2   e: 3   t: 5
# s: 3   e: 1   t: 2
# s: 3   e: 4   t: 4
# s: 4   e: 2   t: 3
# 일단 이거대로 table을 만든다. 플로이드 워셜은 시간이 오래 걸릴 수 있으니 다익스트라로 간다.

graph = [[] for _ in range(n+1)] # 이동 경로 맵
print(*graph, sep='\n')
INF = float('inf') 
distance = [INF] * (n+1) # 최단 거리 table. 

for i in range(1, m+1):
    s, e, t = map(int, sys.stdin.readline().split())
    graph[s].append((e, t))
print(*graph, sep='\n')
# 여기까지 아래와 같이 table이 만들어진다.
# [(2, 4), (3, 2), (4, 7)] => 1에서 2까지 걸리는 시간 4, 1에서 3까지 걸리는 시간 2, ...
# [(1, 1), (3, 5)] => 2에서 1까지 걸리는 시간 1, ....
# [(1, 2), (4, 4)] => ...
# [(2, 3)] => ...

import heapq
def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start)) # 큐에 출발점 push
    distance[start] = 0 # 출발점에서 자기 자신까지의 거리이므로 0으로 설정
    while q:
        dist, now = heapq.heappop(q) # 출발점 기준 0, 1(c)
        if distance[now] < dist: # 기존 distance(출발점 기준 초기화된 distance, 즉 INF)가 더 작으면 skip하고 그렇지 않으면 최솟값 갱신
            continue
        for i in graph[now]: # graph에서 now(출발점 기준 1(c))는 2로 가는 케이스, 3으로 가는 케이스가 있다.
            cost = dist + i[1] # cost는 now까지 가는 거리(출발점 기준 0) + 2, 3으로 가는 각각의 거리
            if cost < distance[i[0]]: # 계산한 cost가 각각 2, 3까지의 distance보다 작으면 이를 갱신하고 큐에 다음 출발점을 push
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

for i in range(n+1):
    # 마을 i에서 다른 마을까지
    dijkstra(i)
    print('go', distance)
    # x에서 각 마을까지
    dijkstra(x)
    print('back', distance)


##########################################################################################
# 플로이드 워셜 => 답 나오긴 하는데 역시나 시간 초과
# INF = float('inf')
# table = [[INF] * (n+1) for _ in range(n+1)]
# for i in range(1, n+1):
#     for j in range(1, n+1):
#         if i == j: table[i][j] = 0

# for i in range(1, m+1):
#     s, e, t = map(int, sys.stdin.readline().split())
#     table[s][e] = t

# for v in range(1, n+1):
#     for s in range(1, n+1):
#         for e in range(1, n+1):
#             table[s][e] = min(table[s][e], table[s][v] + table[v][e])

# distances = [INF] * (n+1)
# for i in range(1, n+1):
#     distances[i] = min(distances[i], table[i][x] + table[x][i])

# print(max(distances[1:]))
##########################################################################################