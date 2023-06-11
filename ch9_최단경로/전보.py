'''
    n개 도시
    x에서 y로 메시지 보내려면 연결된 통로가 있어야 함
    - 통로는 x->y, y->x으로 
    - 양방향이 아니면 통신 불가
    - 다른 통로를 거치면 시간 추가

    도시 c가 보낸 메시지를 받게 되는 도시의 개수
    도시들이 모두  메시지 받는 시간

    n: 도시 개수, m: 통로 개수
    (x, y, z) : 통로 정보(~m + 1개)
    - x->y : 통로 의미
    - z : 메시지 전달 시간
    >>>> x에서 y가는 비용 z라는 뜻

    
'''
import heapq
import sys

input = sys.stdin.readline
INF = int(1e9) # 10억

n, m, start = map(int, input().split()) # 노드, 간선, 시작 노드
graph = [[] for i in range(n + 1)] # 노드 정보 리스트 초기화
distance = [INF] * (n + 1) # 최단거리 테이블 초기화

# 간선 정보 받기
for _ in range(m):
    x, y, z = map(int, input().split())
    graph[x].append((y, z))

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        # 최단 거리가 가장 짧은 노드 pop
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue

        # 인접 노드 확인
        for i in graph[now]:
            cost = dist + i[1]
            
            # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(start)

cnt = 0 # 도달 개수
max_distance = 0 # 도달 개수 중 가장 멀리있는 노드의 최단 거리
for d in distance:
    if d != INF:
        cnt += 1
        max_distance = max(max_distance, d)

print(cnt - 1, max_distance)
# cnt - 1 : 시작 노드 제외