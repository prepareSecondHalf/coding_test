'''
  정점의 개수 n
  간선의 개수 m
  시작 위치 : 정점 번호 v

  input: 두 정점의 번호
'''
# dfs




# bfs
from collections import deque
import sys
input = sys.stdin.readline

n, m, v = map(int, input().split())
graph = [[0] * (n + 1) for _ in range(n + 1)]
visit_list = [0] * (n + 1)
visit_list2 = [0] * (n + 1)

for _ in range(m):
  a, b = map(int, input().split())
  graph[a][b] = graph[b][a] # 입력받는 값에 대해 영형렬에 1삽입(인접리스트생성= 1 <<< 이거 왜 하지??

print(n, m, b, graph)

def dfs(v):
  visit_list[v] = 1
  print(v, end = " ")

  for i in range(1, n + 1):
    if visit_list[i] == 0 and graph[v][i] == 1:
      dfs(i)

def bfs(v):
  q = deque()
  q.append(v)
  visit_list2[v] = 1

  while q:
    v = q.popleft()
    print(v, end = " ")

    for i in range(1, n + 1):
      if visit_list2[i] == 0 and graph[v][i] == 1:
        q.append(i)
        visit_list2[i] = 1


dfs(v)
print()
bfs(v)