'''
    A는 1번 회사 위치
    X번 회사에 방문해 물건 판매
    양방향 이동 가능

    K번 회사 방문
    - 단, X번 회사 방문 전 간다
    - 가장 빠르게

    n : 전체 회사 갯수, m : 경로 개수
    두 회사의 번호 공백(2번째줄 ~ m + 1)
    x, k(m + 2)


    'A'가 K번 회사를 거쳐 X번 회사로 가는 최단경로
'''

# 플로이드 워셜 알고리즘
INF = int(1e9) #10억
n, m = map(int, input().split()) # 노드와 간선 갯수
graph = [[INF] * (n + 1) for _ in range(n + 1)] # 2차원리스트 초기화

for j in range(1, n + 1):
    for i in range(1, n + 1):
        if j == i: #나 to 나
            graph[i][j] = 0

# [초기화] 각 간선 정보 
for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

x, k = map(int, input().split())

# 플로이드 워셜 알고리즘 작동
for p in range(1, n + 1):
    for y in range(1, n + 1):
        for x in range(1, n + 1):
            graph[y][x] = min(graph[y][x], graph[y][p] + graph[p][x])

# 결과
distance = graph[1][k] + graph[k][x]
if distance >= INF:
    # 도달 x
    print("-1")
else:
    # 도달 o
    print(distance)