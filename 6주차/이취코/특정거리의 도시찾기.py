# 백준 18352번
# 도시의 개수 N, 도로의 개수 M, 거리 정보 K, 출발 도시의 번호 X
# a, b (a에서 b로가는 단방향도로)
# 출력 최단거리가 k인 도시의 번호를 한줄에 하나씩 오름차순으로 출력 or 존재하지않을시 -1 출력

from collections import deque
import sys
f = sys.stdin.readline

n, m, k, x = map(int, f().split())
graph = [[] for _ in range(n+1)]
distance = [0] * (n+1)
visited = [False] * (n+1)
# graph, distance, visited를 왜 n개보다 1개 더 만드는지 이해가 가지않음

for _ in range(m):
    a, b = map(int, f().split())
    graph[a].append(b)

def bfs(start):
    answer = []
    q = deque([start])
    visited[start] = True # 출발지점 True처리 
    while q:
        now = q.popleft()
        for i in graph[now]:
            if not visited[i]:
                visited[i] = True
                q.append(i)
                distance[i] = distance[now] + 1 # 출발지점부터의 거리 넣어주기
                # 거리가 k랑 일치하면 answer에 넣어주기
                if distance[i] == k:
                    answer.append(i)
    # if: 목표거리와 거리가 같은 도시가 없으면 -1 출력, else: answer을 오름차순으로 정렬후 for문으로 하나씩 출력
    if len(answer) == 0:
        print(-1)
    else:
        answer.sort()
        for i in answer:
            print(i, end='\n')

bfs(x)