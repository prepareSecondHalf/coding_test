import sys
from queue import Queue

n = int(sys.stdin.readline())

def bfs(cX, cY):  
  que = Queue()
  que.put([cX, cY])
  graph[cX][cY] = 0
  dx = [-1, 1, 0, 0]
  dy = [0, 0, -1, 1]
  while not que.empty():
    a, b = que.get()     

    for i in range(4):
      nX = a + dx[i]
      nY = b + dy[i]

      if (0 <= nX < x) and (0 <= nY < y) and graph[nY][nX] == True:
        print(nY, nX, b, a)
        graph[nY][nX] = False
        que.put([nX, nY])

for _ in range(n):
  x, y, k = map(int, sys.stdin.readline().split())
  graph = [[False for j in range(x)] for i in range(y)]
  cnt = 0

  for i in range(k):
    a, b = map(int, sys.stdin.readline().split())
  
    graph[b][a] = True

  for i in range(y):
    for j in range(x):
      if graph[i][j] == True:
        bfs(i, j)
        graph[i][j] = False
        cnt += 1
        
  print(cnt)