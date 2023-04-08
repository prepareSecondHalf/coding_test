# 백준 14502문제
# 세로 크기 N 가로 크기 M
# 지도의 모양, 0은 빈 칸, 1은 벽, 2는 바이러스
d = [[-1,0],[1,0],[0,-1],[0,1]] # 방향

from collections import deque
import copy
import sys
input = sys.stdin.readline

n, m = map(int,input().split())
lab_map = [list(map(int,input().split())) for _ in range(n)]

result = 0
d = [[-1,0],[1,0],[0,-1],[0,1]]

def bfs():
    queue = deque() 
    test_map = copy.deepcopy(lab_map)
    for i in range(n):
        for k in range(m):
            # 바이러스가 있는요소들 queue에 추가
            if test_map[i][k] == 2:
                queue.append((i,k))

    while queue:
        r,c = queue.popleft()

        # 바이러스 있는 위치 기준 4방향 확인
        for i in range(4):
            dr = r+d[i][0]
            dc = c+d[i][1]

            # 바이러스 기준 상하좌우가 연구소 범위안에 있고 빈벽일경우 바이러스로 변경후 queue에 추가
            if (0<=dr<n) and (0<=dc<m):
                if test_map[dr][dc] == 0:
                    test_map[dr][dc] =2
                    queue.append((dr,dc))

    global result
    count = 0
    # 0인부분 수만큼 count에 +1
    for i in range(n):
        for k in range(m):
            if test_map[i][k] == 0:
                count +=1

    result = max(result, count)


def make_wall(count):
    if count == 3:
        bfs()
        return
    for i in range(n):
        for k in range(m):
            # 빈벽일때 1로바꾸고 재귀함수 실행후 다시 0으로 바꿈
            if lab_map[i][k] == 0:
                lab_map[i][k] = 1
                make_wall(count+1)
                lab_map[i][k] = 0
print(result)


make_wall(0)