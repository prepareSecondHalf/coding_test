'''
  지도 범위는 5X5
  범위를 넘어가는 움직임은 무시

  1~5를 범위
  출발점은 1,1 
  오른쪽 이동은 1,2
  왼쪽 이동은 0, 1
  위쪽 이동은 0, 1
  아래쪽 이동은 2, 1

  이동할 때 마다 좌표 최신화
  최종 위치 산출
'''
n = 5
li = 'R R R U D D'
location = [1, 1]
li = li.split(' ')

def up():
  if location[0] - 1 > 0:
    location[0] -= 1
def down():
  if location[0] + 1 <= n:
    location[0] += 1
def left():
  if location[1] - 1 > 0:
    location[1] -= 1
def right():
  if location[1] + 1 <= n:
    location[1] += 1
def switch(key):
  if "U" == key: up()
  elif "D" == key: down()
  elif "L" == key: left()
  elif "R" == key: right()

for move in li:
  switch(move)
  # print('location: ', location)

print(location[0], location[1])

'''예제코드'''
n = int(input())
x, y = 1, 1
plans = input().split()

dx = [0, 0, -1, -1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

for plan in plans:
  
  for i in range(len(move_types)):
    if plan == move_types[i]:
      nx = x + dx[i]
      ny = y + dy[i]
    
    if nx < 1 or ny < 1 or nx > n or ny > n:
      continue

    x, y = nx, ny

print(x, y)