# n: 도시의 개수, m: 노선의 개수
# 2 ~ m+1줄까지 노선정보 a, b, c( a: 시작지점, b: 도착지점, c걸리는시간)
# c가 0일경우 순간이동, 음수일경우 시간이 거꾸로 간다
# 출력: 1번도시에서 어떠한 도시로 가는과정에서 시간을 무한히 오래전으로 되돌릴수 있다면 첫째줄에 -1 출력 
# 아닐경우 2~n번도시로 가는 가장 빠른시간을 순서대로 출력 해당도시로 가는경로가 없으면 그부분은 -1출력
import sys

n, m = map(int, sys.stdin.readline().split())
INF = int(10e9)
graph = []
distance = [INF] * (n+1)
for _ in range(m):
    graph.append(list(map(int, sys.stdin.readline().split())))

def solution():
    distance[1] = 0 # 1에서 출발이므로 1까지의 거리는 0
    for i in range(1, n+1):
        for j in range(m):
            start, end, time = graph[j][0], graph[j][1], graph[j][2]
            # distance[end]까지의 거리가 start까지의 거리 + 걸리는시간보다 크면(time이 음수일때) 바꿔준다
            if distance[end] > distance[start] + time and distance[start] != INF:
                distance[end] = distance[start] + time
                # i == n 인데 걸리는 시간이 음수이면 시간이 계속 뒤로 돌아가는것이므로 True 리턴 아니면 False 리턴
                if i == n:
                    return True
    return False

if solution():
    print(-1)
else:
    for i in range(2, n+1):
        if distance[i] == INF:
            print(-1)
        else:
            print(distance[i])
