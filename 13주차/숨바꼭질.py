# n: 헛간의 개수, m: 양방향 통로의 개수(양방향
# m줄에 걸쳐 a, b (연결된 헛간)
# 출력: 최단거리가 가장 먼 헛간의 번호, 그 헛간까지의 거리, 그헛간과 같은거리를 갖는 헛간의 개수
import sys

n, m = map(int, sys.stdin.readline().split())
INF = int(10e9)
graph = [[INF] * (n+1) for _ in range(n+1)] # 통로를 입력하기위한 변수
distance = [INF] * n # 최단거리를 입력하기위한 변수
distance[0] = 0
result = []
cnt = 0

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a][b] = 1
    graph[b][a] = 1
    graph[a][a] = 0

for k in range(1, n+1): # k: 경유할 헛간
    for i in range(1, n+1): # i: 출발점
        for j in range(1, n+1): # i: 도착점
            # 기존 graph[i][j]값, k를 경유해서 가는값중 작은값을 적용
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
            if i == 1:
                distance[j-1] = graph[i][j]

# 최대인 헛간번호, 거리 구해서 result에 넣는다
for i in range(n):
    if distance[i] == max(distance):
        result.append(i + 1)
        result.append(distance[i])
        break

# 최대인 헛간 개수 구하기
for i in distance:
    if i == max(distance):
        cnt += 1
result.append(cnt)

# 출력
for i in result:
    print(i, end=' ')


