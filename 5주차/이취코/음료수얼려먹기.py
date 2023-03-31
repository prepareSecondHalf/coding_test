# n: 세로길이, m: 가로길이
import sys


n, m = map(int, sys.stdin.readline().split())
direction = [[0, 1], [0, -1], [-1, 0], [1, 0]] # 방향

graph = []
for _ in range(n):
    graph.append(list(map(int, sys.stdin.readline().strip())))

def dfs(x, y):
    # 범위안에 있을때
    if x >= 0 and x < n and y >= 0 and y < m:
        if graph[x][y] == 0: # 확인하지 않은 좌표
            graph[x][y] = 1 # 확인처리
            for i in range(4): # 4방향
                dfs(x + direction[i][0], y + direction[i][1])
            return True
    return False

result = 0
# 가로세로 크기만큼 dfs 함수 돌려서 True 이면 result +1
for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            result += 1
print(result)