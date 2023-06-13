# 백준 11404 문제
# n: 도시의 개수
# m: 버스의 개수
# 3 ~ m+2번째줄 a: 시작도시, b: 도착도시, c: 비용
# 출력: i번째 줄에 속하는 j번째 숫자는 i에서 j까지가는 최소비용 갈수없는 경우 그자리 0을 출력
import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
INF = int(10e9)
distance = [[INF] * (n+1) for _ in range(n+1)]
graph = []
for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    distance[a][b] = min(distance[a][b], c) # 기존에 있던 distance[a][b]값과 c값중 작은 값을 삽입

for k in range(1, n+1): # 중간에 경유해서 목적지를 가기위해 추가
    for i in range(1, n+1): # 출발지
        for j in range(1, n+1): # 도착지
            if i == j: # 출발지 == 목적지일경우 0삽입
                distance[i][j] = 0
            else:
                # 기존에 distance[i][j]값과 k를 경유해서 갈수있는 값중 작은 값을 삽입
                distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])

for i in range(1, n+1):
    for j in range(1, n+1):
        # 갈수없는 도시의 경우 0을 출력
        if distance[i][j] == INF:
            print(0, end=' ')
        # 아닐 경우 distance[i][j]
        else:
            print(distance[i][j], end=' ')
    print()