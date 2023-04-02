'''
    정점 개수 n
    간선 개수 m
    간선의 양 끝 점 u, v
    첫째 줄 연결요소 개수 출력
'''

import sys
sys.setrecursionlimit(10**7) # 파이선 재귀제한 (런타임에러) > 허용범위 확장
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)

for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)


def dfs(v):
    visited[v] = True
    for i in graph[v]:
        if visited[i] == False:
            visited[i] = True
            dfs(i)

count = 0
for i in range(1, n + 1):
    if visited[i] == False:
        count += 1
        dfs(i)

print(count)