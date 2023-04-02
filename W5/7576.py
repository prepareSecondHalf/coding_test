# 가끔 시간초과....
from queue import Queue

inp = sys.stdin.readline

x, y = map(int, inp().split())
graph = []
que = Queue()

for i in range(y):
  
  graph.append(list(map(int, inp().split())))
  
  for j in range(x):
    if graph[i][j]==1:
      que.put([i, j])
            
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    while not que.empty():
        a, b = que.get()
        
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0 <= nx < y and 0 <= ny < x and graph[nx][ny]==0:
                que.put([nx, ny])
                graph[nx][ny] = graph[a][b]+1

bfs()

res = max(map(max, graph)) - 1
for i in graph:
    if 0 in i:
        res = -1
print(res)

# 개선 코드
import sys
from collections import deque

inp = sys.stdin.readline

x, y = map(int, inp().split())
graph = []
que = deque()
for i in range(y):
  
  graph.append(list(map(int, inp().split())))
  
  for j in range(x):
    if graph[i][j] == 1:
      que.append([i, j])
            
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    while que:
        a, b = que.popleft()
        
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0 <= nx < y and 0 <= ny < x and graph[nx][ny]==0:
                que.append([nx, ny])
                graph[nx][ny] = graph[a][b]+1
bfs()
res = max(map(max, graph)) - 1

for row in graph:
    if 0 in row:
        res = -1
print(res)