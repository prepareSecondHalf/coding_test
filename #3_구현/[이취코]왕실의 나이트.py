'''
  나이트가 이동할 수 있는 경우의 수를 구하라

  8x8
  행: a~h
  열: 1~8
  나이트 이동 방법
  1: 수평 두 칸 후 수직 한 칸
  2: 수직 두 칸 후 수평 한 칸
'''
n = input()
global index

location = [1, 1]
def reDefine(item):
  global index
  key = {"a": 1, "b": 2, "c": 3, "d":4, "e": 5, "f": 6, "g":7, "h": 8 }
  idx = item[0]
  index = str(key[idx]) + str(item[1]) 

def up():
  if location[0] - 1 > 0:
    location[0] -= 1
  else: False
def down():
  if location[0] + 1 <= n:
    location[0] += 1
  else: False
def left():
  if location[1] - 1 > 0:
    location[1] -= 1
  else: False
def right():
  if location[1] + 1 <= n:
    location[1] += 1
  else: False

move_types = [move_type1, move_type2, move_type3, move_type4, move_type5, move_type6, move_type7, move_type8]
move_type1 = [up(), up(), left()]
move_type2 = [up(), up(), right()]
move_type3 = [down(), down(), left()]
move_type4 = [down(), down(), right()]
move_type5 = [left(), left(), up()]
move_type6 = [left(), left(), down()]
move_type7 = [right(), right(), up()]
move_type8 = [right(), right(), down()]

for type in move_types:
  for move in type:
    

''' 예시 코드 '''
input_data = input()
row = int(input_data[1])
column = int(ord(input_data[0])) - int(ord('a')) + 1

steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]

result = 0
for step in steps:
  next_row = row + step[0]
  next_column = column + step[1]

  if (next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8):
    result += 1

print(result)