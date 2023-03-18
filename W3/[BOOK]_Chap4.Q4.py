import sys

# mx, my = sys.stdin.readline().split()
mx, my = 4, 4

# x, y, d = sys.stdin.readline().split()
x, y, d = 1, 1, 0

# 북 동 남 서
xStep = [0, 1, 0, -1] 
yStep = [-1, 0, 1, 0]

cnt = 1
falseArea = 0

# maps = []
maps = [
  ['1', '1', '1', '1'],
  ['1', '0', '0', '1'],
  ['1', '1', '0', '1'],
  ['1', '1', '1', '1']
]

# for i in range(my):
#   maps.append(sys.stdin.readline().split())

while True:
  d -= 1
  if d < 0:
    d = 3

  moveX, moveY = x + xStep[d], y + yStep[d]
  
  if maps[moveX][moveY] == '0':
    maps[moveX][moveY] = '1'
    x, y = moveX, moveY
    cnt += 1
    falseArea = 0
  else:
    falseArea += 1

  if falseArea == 4:
    moveX, moveY = x - xStep[d], y - yStep[d]

    if maps[moveX][moveY] == '0':
      x, y = moveX, moveY
    else:
      break

    falseArea = 0

print(cnt)