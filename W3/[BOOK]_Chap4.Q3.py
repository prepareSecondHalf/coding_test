import sys
input = sys.stdin.readline()

x = int(ord(input[0]) - 96)
y = int(input[1])

step = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]

cnt = 0

for i in step:
  moveX = x + i[0]
  moveY = y + i[1]

  if (moveX >= 1 and moveX <= 8) and (moveY >= 1 and moveY <= 8):
    cnt += 1

print(cnt)