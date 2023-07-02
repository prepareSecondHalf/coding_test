from collections import deque
import sys
input = sys.stdin.readline

for tc in range(int(input())):
    N = int(input())
    indegree = [0] * (N + 1)
    graph = [[False] * (N + 1) for i in range(N + 1)]

    data = list(map(int, input().split()))

    for i in range(N):
        for j in range(i + 1, N):
            graph[data[i]][data[j]] = True
            indegree[data[j]] += 1

    M = int(input())
    for i in range(M):
        a, b = map(int, input().split())

        if graph[a][b]:
            graph[a][b] = False
            graph[b][a] = True
            indegree[a] += 1
            indegree[b] -= 1
        else:
            graph[a][b] = True
            graph[b][a] = False
            indegree[a] -= 1
            indegree[b] += 1

    result = []
    q = deque()

    for i in range(1, N + 1):
        if indegree[i] == 0:
            q.append(i)

    certain = True
    cycle = False

    for i in range(N):
        if len(q) == 0:
            cycle = True
            break
        if len(q) > 1:
            certain = False
            break

        now = q.popleft()
        result.append(now)

        for j in range(1, N + 1):
            if graph[now][j]:
                indegree[j] -= 1

                if indegree[j] == 0:
                    q.append(j)

    if cycle:
        print("IMPOSSIBLE")
    elif not certain:
        print('?')
    else:
        for i in result:
            print(i, end=' ')
        print()