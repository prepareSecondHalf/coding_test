# 체스판 위에 한 나이트가 놓여져 있다. 
# 나이트가 한 번에 이동할 수 있는 칸은 아래 그림에 나와있다. 
# 나이트가 이동하려고 하는 칸이 주어진다. 
# 나이트는 몇 번 움직이면 이 칸으로 이동할 수 있을까?

# 입력의 첫째 줄에는 테스트 케이스의 개수가 주어진다.
# 각 테스트 케이스는 세 줄로 이루어져 있다. 
# 첫째 줄에는 체스판의 한 변의 길이 l(4 ≤ l ≤ 300)이 주어진다. 
# 체스판의 크기는 l × l이다. 
# 체스판의 각 칸은 두 수의 쌍 {0, ..., l-1} × {0, ..., l-1}로 나타낼 수 있다. 
# 둘째 줄과 셋째 줄에는 나이트가 현재 있는 칸, 나이트가 이동하려고 하는 칸이 주어진다.

# 각 테스트 케이스마다 나이트가 최소 몇 번만에 이동할 수 있는지 출력한다.


# 최단 경로 찾기 => BFS
from collections import deque

# 나이트가 이동 가능한 방향의 쌍
dx = [-2, -2, -1, -1, 1, 1, 2, 2]
dy = [-1, 1, -2, 2, -2, 2, -1, 1]

# BFS
def bfs(l, start, end):
    queue = deque()
    queue.append(start)
    # 맵을 만들고 False(미탐색)로 초기화
    visited = [[False] * l for _ in range(l)]
    # start 지점은 현재 위치한 곳이므로 기본 True
    visited[start[0]][start[1]] = True
    count = 0

    while queue:
        for _ in range(len(queue)):
            x, y = queue.popleft()
            # queue의 가장 왼쪽 튜플(start)이 end와 같으면 종료
            if (x, y) == end:
                return count
            for i in range(8):
                # 아니면 현 위치에서 이동 가능한 케이스 전부 탐색
                nx = x + dx[i]
                ny = y + dy[i]
                # 맵을 벗어나면 넘어감
                if nx < 0 or ny < 0 or nx >= l or ny >= l:
                    continue
                # 아직 탐색 안 했으면 queue에 넣고 True로 변환
                # queue에 추가함으로써 현 위치(start)에서 탐색이 끝나면 이후 추가된 위치에서 bfs를 재실행
                if not visited[nx][ny]:
                    queue.append((nx, ny))
                    visited[nx][ny] = True
        count += 1

# 입력
import sys
n = int(sys.stdin.readline())
for i in range(n):
    l = int(sys.stdin.readline())
    start = tuple(map(int, sys.stdin.readline().split()))
    end = tuple(map(int, sys.stdin.readline().split()))
    print(bfs(l, start, end))