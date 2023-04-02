'''
  첫째 줄 = 컴퓨터 수
  둘째 줄 = 연결되어 있는 컴퓨터 쌍의 수
  나머지 = 연결되어 있는 컴퓨터 번호 쌍
'''

from collections import deque
n = int(input()) # 컴퓨터의 갯수
v = int(input()) # 연결선의 갯수
graph = [[] for i in range(n + 1)] # 그래프 초기화
visited = [0] * (n + 1) # 방문한 컴퓨터인지 표시

for i in range(v):
    a, b = map(int, input().split())
    graph[a] += [b] # a에 b 연결
    graph[b] += [a] # b에 a 연결 (양방향)
visited[1] = 1 # 1번 컴퓨터부터 시작이니 방문 표시

Q = deque([1])
while Q:
  c = Q.popleft()

  for nx in graph[c]:
     if visited[nx] == 0:
        Q.append(nx)
        visited[nx] = 1
print(sum(visited) - 1)

