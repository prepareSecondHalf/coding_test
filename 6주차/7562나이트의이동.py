# t: 테스트 케이스 수
# sx, sy: 현재 나이트 좌표
# ax, ay: 가야할 나이트 좌표
from collections import deque
import sys
dx = [-1, -2, -2, -1, 1, 2, 2, 1]
dy = [2, 1, -1, -2, -2, -1, 1, 2]
def bfs(sx, sy, ax, ay):
    q = deque()
    q.append([sx, sy])
    while q:
        a, b = q.popleft()
        if a == ax and b == ay:
            print(s[ax][ay])
            return
        for i in range(8):
            x = a + dx[i]
            y = b + dy[i]
            if 0 <= x < n and 0 <= y < n and s[x][y] == 0: # 범위안 and 이동하지않았던 좌표
                q.append([x, y])
                s[x][y] = s[a][b] + 1 # 이동한칸에 이동전 좌표의 숫자 + 1 을 해서 카운트
t = int(sys.stdin.readline())
for i in range(t):
    n = int(sys.stdin.readline())
    sx, sy = map(int, sys.stdin.readline().split())
    ax, ay = map(int, sys.stdin.readline().split())
    s = [[0] * n for i in range(n)]
    bfs(sx, sy, ax, ay)