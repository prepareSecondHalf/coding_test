from collections import deque
n, m = map(int, input().split())
graph = []

for i in range(n):
  graph.append(list(map(int, input())))

# print(graph)

# dy = [-1, 1, 0, 0]
# dx = [0, 0, -1, 1]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
  queue = deque()
  queue.append((x, y))

  while deque:
    x, y = queue.popleft()

    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      # print(ny, nx)

      if nx < 0 or ny < 0 or nx >= n or ny >= m:
        continue

      # if graph[ny][nx] == 0:
      if graph[nx][ny] == 0:
        continue

      # if graph[ny][nx] == 1:
      if graph[nx][ny] == 1:
        graph[nx][ny] = graph[x][y] + 1
        queue.append((nx, ny))


    return graph[n - 1][m - 1]


print(bfs(0, 0))


''' 정답 '''
from collections import deque
n, m = map(int, input().split())
graph = []

for i in range(n):
  graph.append(list(map(int, input())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
  queue = deque()
  queue.append((x, y))

  while queue:
    x, y = queue.popleft()

    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      if nx < 0 or ny < 0 or nx >= n or ny >= m:
        continue

      if graph[nx][ny] == 0:
        continue

      if graph[nx][ny] == 1:
        graph[nx][ny] = graph[x][y] + 1
        queue.append((nx, ny))

  return graph[n - 1][m - 1]

print(bfs(0, 0))


'''
  78번째 리턴의 인덴트 때문에 자꾸 다른 값이 반환되었다. 
  내 시간 돌리도...
'''