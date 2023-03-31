# 정점: n, 간선: m, 정점번호: v
# DFS = 깊이 우선 탐색  BFS = 너비 우선 탐색
N,M,V = map(int,input().split())

#간선 리스트
graph = [[0]*(N+1) for _ in range(N+1)]
for i in range (M):
    a,b = map(int,input().split())
    graph[a][b] = graph[b][a] = 1 #양방향 처리


visited1 = [0]*(N+1)
visited2 = [0]*(N+1)

#dfs 함수 만들기
def dfs(V):
    visited1[V] = 1 #확인한 번호 제외처리
    print(V, end=' ')
    # V랑 연결된 번호 찾기
    for i in range(1, N+1):
        if graph[V][i] == 1 and visited1[i] == 0:
            dfs(i)

#bfs 함수 만들기
def bfs(V):
    line = [V]
    visited2[V] = 1 #확인한 번호 제외처리
    while line:
        V = line.pop(0) #먼저 들어온번호부터 제거후 V변수로 돌려받기
        print(V, end = ' ')
        for i in range(1, N+1):
            if(visited2[i] == 0 and graph[V][i] == 1):
                line.append(i)
                visited2[i] = 1 #확인한 번호 제외처리

dfs(V)
print()
bfs(V)