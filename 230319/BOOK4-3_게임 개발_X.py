# 캐릭터가 있는 장소는 1 x 1 크기의 정사각형으로 이루어진 N x M 크기의 직사각형으로, 각 칸은 육지 또는 바다
# 캐릭터는 동서남북 중 하나를 바라본다.
# 각 칸은 (A, B)로 나타낼 수 있고, A는 북쪽으로부터 떨어진 칸의 개수, B는 서쪽으로부터 떨어진 칸의 개수이다.
# 바다에는 갈 수 없고 캐릭터는 다음 매뉴얼을 따라 움직인다.
# 1. 현 위치에서 현 방향을 기준으로 왼쪽 방향(반시계 방향으로 90도 회전)한 방향부터 갈 곳을 정한다.
# 2. 바로 왼쪽에 아직 안 간 칸이 있으면 그 방향으로 한 칸 전진, 없으면 회전만 하고 1단계로
# 3. 네 방향 모두 가 본 칸이거나 바다라면, 바라보는 방향을 유지한 채 뒤로 한 칸 가고 1단계로 가되, 뒤쪽 방향이 바다면 멈춘다.
# 매뉴얼에 따라 캐릭터를 이동한 후, 방문한 칸의 수를 출력하라

# 첫째 줄에 맵의 세로 크기 N과 가로 크기 M이 공백으로 구분되어 입력(3 <= N, M <= 50)
# 둘째 줄에 게임 캐릭터가 있는 칸의 좌표 (A, B)와 바라보는 방향 d가 각각 공백으로 구분되어 입력
# d는 (0, 1, 2, 3) 순으로 (북, 동, 남, 서)
# 셋째 줄부터 맵 정보 입력, N개의 줄에 맵의 상태가 북~남 순으로 주어지며 각 줄은 서~동, 
# 맵의 외곽은 항상 바다이며 0은 육지, 1은 바다
# 게임 캐릭터가 위치하는 곳은 항상 육지

# 첫째 줄에 이동 후 캐릭터가 방문한 칸의 수를 출력

import sys
n, m = map(int, sys.stdin.readline().split()) # 맵 크기 (n, m)
a, b, d = map(int, sys.stdin.readline().split()) # 현위치(a, b) 및 방향(d)
map_data = []
for i in range(n):
    map_data.append(list(map(int, sys.stdin.readline().split())))

# 풀이: 각 변수들의 범위가 좁으므로 완전 탐색을 하면 될 것이다... 시키는대로 하자
# 캐릭터가 지나갈 수 있는 칸은 0, 못 지나가는 칸은 1이므로 지나간 뒤에 1로 바꾸면 될 듯?
# 은 다시 뒤로 갈 가능성도 있으니 -1로 해 두고, 마지막에는 -1들을 모두 찾아 더한 뒤 양수로 만들어서 출력하면 되겠다.

# 1. 방향: 북0 동1 남2 서3인데 캐릭터가 회전하는 방향은 반대(현재 방향 -1)이므로
#         북0 서-1 남-2 동-3 이라고 생각하자
# 2. 스텝: 북, 서로 이동하는 경우는 -1, 남, 동으로 이동하는 경우는 +1이다

# 돌아갈 때를 대비해 prev position 저장
prev_positions = [[a, b]]
prev_d = d
def get_next(curr_d, curr_x, curr_y):
  if curr_d == 0:
    return curr_x, curr_y - 1
  elif curr_d == -1:
    return curr_x - 1, curr_y
  elif curr_d == -2:
    return curr_x, curr_y + 1
  elif curr_d == -3:
    return curr_x + 1, curr_y

can_progress = True
curr_x, curr_y = a, b
curr_d = d
conquered = 0
while can_progress:
  # step1 방향 전환
  curr_d -= 1

  # step2
  next_target = map_data[get_next(curr_d, curr_x, curr_y)[0]][get_next(curr_d, curr_x, curr_y)[1]]
  if next_target == 0:
    # step2-1. 0이면 진행(원래 있던 자리를 -1로 변경하고 현재 위치를 target으로 변경)
    map_data[get_next(curr_d, curr_x, curr_y)[0]][get_next(curr_d, curr_x, curr_y)[1]] = -1
    conquered += 1
    curr_x, curr_y = get_next(curr_d, curr_x, curr_y)
  else:
    # step2-2. 1 or -1이면 step1으로 돌아감

    # step3 네 방향 다 뒤졌는데 없다? 뒤로 한 칸 가야 됨(방향 및 위치 초기화)
    if curr_d == prev_d - 4:
      curr_d = prev_d
      curr_x, curr_y = prev_positions[-1][0], prev_positions[-1][1]
      prev_positions.pop()
      # 다시 읽어보니, 뒤로 간다고 안 간 걸로 되는 것은 아니다.
    continue
print(conquered)


# 모범 답안
n, m = map(int, sys.stdin.readline().split())
d = [[0] * m for _ in range(n)]
x, y, direction = map(int, sys.stdin.readline().split())
d[x][y] = 1 # 현 좌표 방문

array = []
for i in range(n):
  array.append(list(map(int, sys.stdin.readline().split())))

# 동서남북
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 왼쪽 회전
def turn_left():
  global direction
  direction -= 1
  if direction == -1:
    direction = 3

# 이동 시작
count = 1
turn_time = 0
while True:
  turn_left()
  nx = x + dx[direction]
  ny = y + dy[direction]
  # 회전 후, 정면에 가 보지 않은 칸이 존재하는 경우 => 이동
  if d[nx][ny] == 0 and array[nx][ny] == 0:
    d[nx][ny] = 1
    x = nx
    y = ny
    count += 1
    turn_time = 0
    continue
  else:
    # 회전 후, 정면에 가 보지 않은 칸이 없거나 바다인 경우 => 다시 회전
    turn_time += 1
  if turn_time == 4:
    # 네 방향 모두 가 봤거나 바다인 경우
    nx = x - dx[direction]
    ny = y - dy[direction]
    # 뒤로 갈 수 있으면 뒤로 이동
    if array[nx][ny] == 0:
      x = nx
      y = ny
    # 뒤가 바다인 경우
    else:
      break
    turn_time = 0
print(count)