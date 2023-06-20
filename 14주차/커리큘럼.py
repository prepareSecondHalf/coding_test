# n: 들고자 하는 강의의 수
# 강의시간, ...들어야하는강의번호들, -1
# 출력: n개의 강의에 대하여 수강하기까지 걸리는 최소시간을 한줄에 하나씩 출력(강의를 동시에 들을수 있다고 가정)
from collections import deque
import sys

si = sys.stdin.readline

n = int(si())

time = [0] * (n + 1) # 각 강의당 소요시간
res = [0] * (n + 1) # 먼저들어야하는 강의가 있을때 각 강의 완료까지 소요시간
indegree = [0] * (n + 1)  # 진입차수
graph = [[] for i in range(n + 1)]

for i in range(1, n + 1):
    t, *node = map(int, si().split()) # t = 강의시간, node = ...선행해야하는 강의, -1
    time[i] = t
    res[i] = t

    # graph에 다른강의를 완료하기위해 해당강의를 수강해야하면 강의번호를 넣어주고 indegree에서 선행강의 +1
    for j in range(len(node) - 1): # 마지막 -1 제외
        graph[node[j]].append(i) # graph에 다른강의를 완료하기위해 해당강의를 수강해야하면 강의번호를 넣어줌 
        indegree[i] += 1


def topology_sort():
    queue = deque()

    # 선행되지않아도 되는강의들 queue에 추가
    for i in range(1, n + 1):
        if indegree[i] == 0:
            queue.append(i)

    while queue:
        x = queue.popleft()
        # x를 완료하기 위해 선행해야하는 강의들을 확인
        for y in graph[x]:
            indegree[y] -= 1
            # y 총소요시간 = 기존 총 소요시간, x총소요시간 + y강의시간중 최대값으로 갱신해나감
            res[y] = max(res[y], res[x] + time[y])
            # y확인이 끝나면 queue에 y추가
            if indegree[y] == 0:
                queue.append(y)


topology_sort()

for i in range(1, n + 1):
    print(res[i])


