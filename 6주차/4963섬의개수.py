import sys
# setrecursionlimit() 함수 재귀 최대 깊이 기본설정 = 1000회 , 최대깊이 10**9로 설정, 미설정시 RecursionError 발생 가능
sys.setrecursionlimit(10**9)

graph = []
direction = [[0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1]]

#  연결되어있는부분을 전부 2로 바꿔주고 1을 반환
def dfs(x, y, w, h): #x y: 확인하려는 좌표, w h: 전체 크기
    graph[x][y] = 2
    for i in range(8):
        nx, ny = x + direction[i][0], y + direction[i][1]
        if 0 <= nx < h and 0 <= ny < w:
            if graph[nx][ny] == 1:
                dfs(nx, ny, w, h)
    return 1
    

while True:
    w, h = map(int, sys.stdin.readline().split())
    count = 0
    if w == 0 and h == 0:
        break
    for _ in range(h):
        line = list(map(int, sys.stdin.readline().split()))
        graph.append(line)
    for j in range(h):
        for k in range(w):
            if graph[j][k] == 1:
                count += dfs(j, k, w, h)
    print(count)
    graph = []
