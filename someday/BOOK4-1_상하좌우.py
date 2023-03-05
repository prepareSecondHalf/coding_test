# 여행가 A는 N x N 크기의 정사각형 공간 위에 서 있다.
# 이 공간은 1 X 1 크기의 정사각형으로 나누어져 있다.
# 가장 왼쪽 위 좌표는 (1, 1)이며, 가장 오른쪽 아래 좌표는 (N, N)에 해당한다.
# 여행가 A는 상, 하, 좌, 우 방향으로 이동할 수 있으며 시작 좌표는 항상 (1, 1)이다.
# 계획서에는 하나의 줄에 띄어쓰기를 기준으로 L, R, U, D 중 하나의 문자가 반복적으로 적혀 있다.
# 각각 왼쪽, 오른쪽, 위, 아래로 한 칸씩 이동한다는 의미로, 정사각형의 공간을 벗어나는 움직임은 무시된다.
# 계획서가 주어졌을 때 A가 최종적으로 도착할 지점의 좌표를 출력하는 프로그램을 작성하시오

# 첫째 줄에 공간의 크기 N, 둘째 줄에 계획서 내용이 주어진다.
# 첫째 줄에 A가 최종적으로 도착할 지점의 좌표를 공백으로 구분하여 출력한다.

import sys
n = int(sys.stdin.readline())
steps = list(sys.stdin.readline().split())

# 풀이 1: 단순 반복문 => 시간 복잡도가 N이므로 큰 문제 없어 보인다.
currX, currY = 1, 1
for step in steps:
    if step == 'L':
        if currX == 1: continue
        else: currX -= 1
    elif step == 'R':
        if currX == n: continue
        else: currX += 1
    elif step == 'U':
        if currY == 1: continue
        else: currY -= 1
    elif step == 'D':
        if currY == n: continue
        else: currY += 1
print('first: ', currX, currY)

# 모범 답안 참고: 약간의 아이디어를 보태면 코드가 더 짧아짐
directions = ['L', 'R', 'U', 'D']
directionX = [-1, 1, 0, 0]
directionY = [0, 0, -1, 1]
currentX, currentY = 1, 1

for step in steps:
    for direction_index in range(len(directions)):
        if step == directions[direction_index]:
            currentX += directionX[direction_index]
            currentY += directionY[direction_index]
            if currentX == 0: currentX = 1
            if currentY == 0: currentY = 1
            if currentX == n+1: currentX = n
            if currentY == n+1: currentY = n
print('second: ', currentX, currentY)

# 모범 답안
x, y = 1, 1
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

for step in steps:
    for i in range(len(move_types)):
        if step == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
        if nx < 1 or ny < 1 or nx > n or ny > y:
            continue
        x, y = nx, ny
print('book: ', x, y)