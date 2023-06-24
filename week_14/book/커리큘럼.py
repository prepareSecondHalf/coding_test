import sys
from collections import deque
from copy import deepcopy

N = int(sys.stdin.readline())
indegree = [0] * (N + 1)
times = [0] * (N + 1)

graph = [[] for i in range(N + 1)]

for i in range(1, N + 1):
    data = list(map(int, sys.stdin.readline().strip().split()))
    times[i] = data[0]

    for j in data[1:-1]:
        indegree[i] += 1
        graph[j].append(i)

# time 을 어떻게 써먹을지 모르겠다.
def topology_sort():
    result = []
    q = deque()

    for i in range(1, N + 1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        result.append(now)

        for i in graph[now]:
            indegree[i] -= 1

            if indegree[i] == 0:
                q.append(i)

    for i in result:
        print(i)

topology_sort()

# 정답
def topology_sort():
    result = deepcopy(times)
    q = deque()

    for i in range(1, N + 1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()

        for i in graph[now]:
            result[i] = max(result[i], result[now] + time[i])
            indegree[i] -= 1

            if indegree[i] == 0:
                q.append(i)

    for i in (1, N + 1):
        print(result[i])