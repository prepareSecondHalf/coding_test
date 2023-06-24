from collections import deque
import copy

n = int(input())
indegree = [0] * (n + 1)
graph = [[] for _ in range(n + 1)]
time = [0] * (n + 1) # 각 강의 시간을 관리 필요성을 인지 못했음

for i in range(1, n + 1):
  info = list(map(int, input().split()))
# 여기서 막힘 : 두 개 이상의 입력값이 있을 경우 처리
  time[i] = info[0]
  for x in info[1:-1]:
    indegree[i] += 1
    graph[x].append(i)

def topology_sort():
  result = copy.deepcopy(time)
  q = deque()

  for i in range(1, n + 1):
    if indegree[i] == 0:
      q.append(i)

  while q:
    now = q.popleft()
    for i in graph[now]:
      result[i] = max(result[i], result[now] + time[i])
      indegree[i] -= 1
      if indegree[i] == 0:
        q.append(i)

  for i in range(1, n + 1):
    print(result[i])

topology_sort()