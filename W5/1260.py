import sys
from queue import Queue

n, m, z = map(int, sys.stdin.readline().split())

graph = [[0 for j in range(n+1)] for i in range(n+1)]
visitedDfs = [False for i in range(n+1)]

for i in range(m):
  a, b = map(int, sys.stdin.readline().split())

  graph[a][b] = graph[b][a] = 1

def dfs(node):
  visitedDfs[node] = True
  print(node, end=' ')

  for next in range(1, n+1):
    if not visitedDfs[next] and graph[node][next]:
      dfs(next)

def bfs(node):
  visitedBfs = [False for _ in range(n+1)]
  que = Queue()
  visitedBfs[node] = True
  que.put(node)
  while not que.empty():
    curr = que.get()
    
    print(curr, end = ' ')
    for next in range(1, n+1):
      if not visitedBfs[next] and graph[curr][next]:
        visitedBfs[next] = True
        que.put(next)
        
dfs(z)
print()
bfs(z)