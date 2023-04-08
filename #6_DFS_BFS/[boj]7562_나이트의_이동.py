'''
테스트 개수

테케는 세 줄로 이뤄짐 (한 변의 길이, 나이트 현재 칸, 나이트 이동하려는 칸)
=> 테케마다 나이트 최소 이동 회수 출력
'''

n = int(input())
for i in range(n): # 테케 개수만큼 반복
    l = int(input())
    field = list()
    visited = list()

    for i in range(l):
        field.append([0] * l)
        visited.append([0] * l)

    
    queue = deque()
    x, y = map(int, input().split()) 
    w, z = map(int, input().split()) 
    queue.append((x, y)) # 큐에 시작 위치 추가
    visited[x][y]

    # bfs는 탐색 노드를 큐에 삽입하고 방문 처리 후, 큐를 노드에서 꺼내 해당 노드의 인접 노드 중 바운하지 않은 노드를 모두 큐에 삽입하는 것
    while queue: # 큐에 아무것도 없을 때까지
        x, y = queue.popleft() # 처음 입력된 좌표를 꺼냄
        if x == w and y == z:
            break
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i] # 현재값 + 이동값으로 신규 위치 구함

            
            if nx < 0 or ny < 0 or nx >= 1 or ny >= 1: 
                continue
            
            
            if field[nx][ny] == 0:
                field[nx][ny] = field[x][y] + 1 # 신규 좌표값에 방문 처리
                queue.append((nx,ny)) # 방문한 좌표 큐에 추가
    print(field[w][z])
    
from collections import deque
import sys
input = sys.stdin.readline

# 나이트 이동 방향
dx = [-1, -2, -2, -1, 1, 2, 2, 1]
dy = [2, 1, -1, -2, -2, -1, 1, 2]

def bfs(sx, sy, ax, ay):
    q = deque()
    q.append([sx, sy])
    s[sx][sy] = 1
    while q:
        a, b = q.popleft()
        if a == ax and b == ay: # 꺼낸 좌표가 목표 좌표면 종료
            print(s[ax][ay] -1)
            return
        for i in range(8): # 8방향에 대한 이동 값 
            x = a + dx[i]  # 현재값 + 이동값으로 신규 위치 구함
            y = b + dy[i]  # 현재값 + 이동값으로 신규 위치 구함

            # 신규 위치 범위 안에 있는지 + 방문하지 않은 곳이라면
            if 0 <= x < n and 0 <= y < n and s[x][y] == 0: 
                q.append([x, y])
                s[x][y] = s[a][b] + 1 # 해당 좌표에 현재까지 이동 회수 + 1

t = int(input()) # 테스트 케이스 개수
for i in range(t):
    n = int(input()) # 체스판 크기 사용될 값
    sx, sy = map(int, input().split()) # 시작 위치
    ax, ay = map(int, input().split()) # 목표 위치
    s = [[0] * n for i in range(n)]
    bfs(sx, sy, ax, ay)