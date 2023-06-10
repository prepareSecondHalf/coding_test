# n: 도시의 개수, m: 통로의 개수, c: 메시지를 보내고자 하는 도신
# 2 ~ m+1줄까지 x,y: 이어져있는 도시 ,z: 걸리는 시간
# 출력: c에서 보낸 메시지를 받는 도시의 총 개수, 총 걸리는 시간

# 정답
import heapq
import sys

input = sys.stdin.readline
INF = 987654321

n, m, start = map(int, input().split())
graph = [[] for _ in range(n+1)]
distance = [INF] * (n+1)

for _ in range(m):
    # x,y: 이어져있는 도시 ,z: 걸리는 시간
    x, y, z = map(int, input().split())
    # graph[x]에 이여져있는 도시와 걸리는 시간을 묶어서 삽입
    graph[x].append((y, z))

    def dijkstra(start):
        q = []

        # q에 (0, start)삽입후 start 지점 거리 0으로 초기화
        heapq.heappush(q, (0, start))
        distance[start] = 0


        while q:
            # q에서 뽑아서 도시가 이어져 있지 않으면 for문을 실행
            dist, now = heapq.heappop(q)
            if distance[now] < dist:
                continue

            # 시작지점이랑 이어져있는 도시들로 for문을 실행
            for i in graph[now]:
                cost = i[1]
                # 걸리는 거리가 distance에 들어있는 거리보다 작으면 cost로 바꿔주고 q에 (거리, 도시좌표) 삽입을 반복
                if cost < distance[i[0]]:
                    distance[i[0]] = cost
                    heapq.heappush(q, (cost, i[0]))

dijkstra(start)

count = 0 # 메시지를 받는 도시의 개수

max_distance = 0 # 총 걸리는 시간
# distance에 들어있는 거리가 INF가 아니면 count+1, max_distance에 더큰 거리 삽입
for d in distance:
    if d != INF:
        count += 1
        max_distance = max(max_distance, d)

# count에 start지점까지의거리 0이 포함되어있으므로 count는 1을 빼준다
print(count - 1, max_distance)




# 오답
# import sys
# 
# n, m, c = map(int, sys.stdin.readline().split())
# INF = int(10e9)
# graph = [[INF] * (n+1) for _ in range(n+1)]
# count = 0
# time = 0
# 
# for _ in range(m):
#     x, y, z = map(int, sys.stdin.readline().split())
#     graph[x][y] = z
#     graph[y][x] = z
# 
# for i in range(1, n+1):
#     for j in range(1, n+1):
#         for k in range(1, n+1):
#             graph[j][k] = min(graph[j][k], graph[j][i] + graph[i][k]) 
# 
# for i in range(1, n+1):
#     for j in range(1, n+1):
#         if graph[i][j] != INF:
#             count += 1
#             time = max(time, graph[i][j])
# print(count, time)