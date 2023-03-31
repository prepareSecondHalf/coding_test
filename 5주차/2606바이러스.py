# v: 컴퓨터수, e: 연결하는 선의 수
import sys

v = int(sys.stdin.readline())
e = int(sys.stdin.readline())
graph = [[] for _ in range(v+1)]
for _ in range(e):
    a, b = map(int, input().split())
    # 연결된 컴퓨터의 정보가 언제가 1부터 등장한다는 보장 x
    graph[a].append(b)
    graph[b].append(a)


def dfs(x):
    global count
    visited[x] = True #확인한번호는 True처리
    count += 1
    # 재귀함수로 연결되어있는 번호 확인
    for i in graph[x]:
        if visited[i]:
            continue
        dfs(i)

count = 0
visited = [False for _ in range(v+1)]
dfs(1) #1번컴퓨터 바이러스
print(count-1)