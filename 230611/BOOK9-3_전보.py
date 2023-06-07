# 어떤 나라에는 N개의 도시가 있다. 각 도시는 보내고자 하는 메시지가 있는 경우 다른 도시로 전보를 보낸다.
# X에서 Y로 보내고자 한다면 통로가 설치되어 있어야 한다.
# 통로는 단방향이며 일정 시간이 소요된다.
# 어느 날 C 도시에서 위급 상황이 발생해 최대한 많은 도시로 메시지를 보내려 한다.
# 메시지는 C에서 출발해 최대한 멀리 퍼져 나갈 것이다.
# 각 도시명과 통로에 대한 정보가 주어졌을 때, C에서 보낸 메시지를 받게 되는 도시의 개수는 몇 개이고 각각 걸리는 시간이 얼마인지 계산하시오

# 입력
# 첫째 줄에 도시의 개수 N, 통로의 개수 M, 메시지를 보내고자 하는 C가 주어진다. (1 <= N <= 30000) (1 <= M <= 200000) (1 <= C <= N)
# 둘째 줄부터 M+1번째 줄에 걸쳐 통로에 대한 정보 X, Y, Z가 주어진다. 이는 X에서 Y로 이어지는 통로가 있으며 Z만큼 시간이 걸린다는 의미이다.
# (1 <= X, Y, <= N) (1 <= Z <= 1000)

# 출력
# 첫째 줄에 C에서 보낸 메시지를 받는 도시의 총 개수와 총 시간을 공백으로 구분하여 출력한다.

import sys
n, m, c = map(int, sys.stdin.readline().split())

# 풀이
# 1. 각 노드와 연결된 노드의 정보를 초기화
graph = [[] for _ in range(n+1)]
INF = float('inf')
# 2. 최단 거리 테이블 초기화(무한)
distance = [INF] * (n+1)
# 3. 간선 정보 입력 (x에서 y로 갈 때 걸리는 시간 z)
for _ in range(m):
    x, y, z = map(int, sys.stdin.readline().split())
    graph[x].append((y, z))
print(*graph, sep='\n')
# 여기까지 작성하면 graph는
# (2, 4)    (3, 2)
# ()        ()
# ()        ()
# distance는 
# [INF, INF, INF, INF]
# 로 초기화된다. (테스트 케이스에서는 1에서 2, 1에서 3으로 가는 케이스밖에 없다.)

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
dijkstra(c)
print(distance)
# 이렇게 하면 distance 배열이 아래와 같이 완성된다.
# [0, 4, 2]

# 1. 메시지를 받는 총 도시의 수는 distance의 길이에서 INF(도달 불가) 또는 0(자기 자신)이 아닌 값들의 수
# 2. 걸리는 총 시간은 가장 큰 값(가장 멀리 있는 도시)
# distance에서 0과 INF를 제거한 뒤에 길이를 구하면 총 도시의 수, 그 중 가장 큰 수를 구하면 걸리는 총 시간이 나온다.
remove_set = { 0, INF }
distance = [dist for dist in distance if dist not in remove_set]
print(distance)

print(len(distance), max(distance))

# TEST CASE
# 3 2 1
# 1 2 4
# 1 3 2