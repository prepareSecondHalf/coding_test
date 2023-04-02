'''
테스트 케이스 개수 t
가로 길이 m, 세로 길이 n, 배추 위치 k
최소 배추흰지렁이 마리 수 출력
'''

import sys
sys.setrecursionlimit(10**9)

t = int(input())
result_list = []

def make_graph(m, n, k):
    graph = [[0] * m for _ in range(n)]
    for _ in range(k):
        x, y = map(int, sys.stdin.readline().split())
        graph[y][x] = 1
    return graph

def dfs(y, x):
    if x <= -1 or x >= m or y <= -1 or y >= n:
        return False

    if graph[y][x] == 1:
        graph[y][x] = 0
        dfs(y - 1, x)
        dfs(y + 1, x)
        dfs(y, x - 1)
        dfs(y, x + 1)
        return True
    return False

for _ in range(t):
    result = 0
    m, n, k = map(int, sys.stdin.readline().split())
    graph = make_graph(m, n, k)

    for i in range(n):
        for j in range(m):
            if dfs(i, j) == True:
                result += 1
    result_list.append(result)

print(*result_list, sep='\n') # * = unpacking 