# n: 학생의 수, m: 도로의 수(단방향), x: 파티하는 마을의 번호
# 2~m+1줄까지 시작점, 끝점, 소요시간
# 출력: x마을을 찍고 다시 자기마을로 돌아오는데 가장오래걸리는 학생의 소요시간
import sys
import heapq
f = sys.stdin.readline
INF = int(1e9)

n, m, x = map(int, f().split()) # n: 학생의 수, m: 도로의 수(단방향), x: 파티하는 마을의 번호
adjList = [[] for _ in range(n+1)]

for i in range(m):
    a, b, c = map(int, f().split()) # 시작점, 끝점, 소요시간
    adjList[a].append((b, c))

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
        
        # 입력받은 도로, 소요시간으로 for문 실행
        for i in adjList[now]:
            cost = dist + i[1] # cost에 소요시간을 넣어준다
            # cost가 현재 distance에 들어있는 거리보다 작으면 바꿔주고 q에 넣어준다
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
    return distance

result = [[]]
time_list = []
# 각지점에서 다른 지점들까지의 거리들을 전부 구해서 result에 넣어준다
for i in range(1,n+1):
    distance = [INF] * (n+1)
    result.append(dijkstra(i))
    
# 위에서 구한 result에서 현재위치에서 x까지의 거리 + x부터 현위치까지의 거리를 합해서 time_list에 넣어주고 최대값 출력
for i in range(1, n+1):
    time_list.append(result[i][x] + result[x][i])

print(max(time_list))




