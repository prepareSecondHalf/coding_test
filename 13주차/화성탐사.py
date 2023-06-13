# t: 테스트 케이스의 수
# n: 탐사공간의 크기 (n * n)
# n줄에 걸쳐 각 칸의 비용
# 출력: [0][0]에서 가장 오른쪽 아래로 이동하는 최소 비용
import heapq
import sys

t = int(sys.stdin.readline())
d = [(0, 1), (0, -1), (-1, 0), (1, 0)] # 상하좌우

for _ in range(t):
    n = int(sys.stdin.readline())
    graph = []
    INF = int(10e9)
    distance = [[INF] * n for _ in range(n)]

    # 맵정보 받기
    for _ in range(n):
        graph.append(list(map(int, sys.stdin.readline().split())))


    q = [(graph[0][0], 0, 0)] # 비용, x좌표, y좌표
    distance[0][0] = graph[0][0]

    while q:
        dist, x, y = heapq.heappop(q)
        # distance[x][y]값이 현재좌표값보다 작으면 뒤에코드를 건너뛴다
        if dist > distance[x][y]:
            continue
            
        for i in range(4): # 상하좌우
            dx, dy = x + d[i][0], y + d[i][1]
            if dx < 0 or dx >= n or dy < 0 or dy >= n:
                continue
            cost = dist + graph[dx][dy]
            # 현재 distance에 들어있는 좌표까지 누적된 비용의 최솟값 > 이동한좌표값 + 이동하기전까지 누적된값
            if distance[dx][dy] > cost:
                distance[dx][dy] = cost
                heapq.heappush(q, (cost, dx, dy)) # q에 삽입후 q에 값이 없을때까지 while문을 다시돌린다
    print(distance[n-1][n-1])




