n = 5
arr = ['U', 'L', 'R', 'R', 'R', 'U', 'D', 'D', 'L']

coor = [1, 1]

for i in arr:

  if i == 'R':
    if coor[1] != n:
      coor[1] += 1
  elif i == 'L':
    if coor[1] != 1:
      coor[1] -= 1
  elif i == 'U':
    if coor[0] != 1:
      coor[0] -= 1
  elif i == 'D':
    if coor[0] != n:
      coor[0] += 1

print(coor[0], coor[1])