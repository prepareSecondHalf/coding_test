#1: 틀림
'''
calculating different kinds of statistics for flats the agency

Reduced total area is the total area of all rooms except for balconies plus one half of balconies total area.

n - 방의 개수, c - 1평당 비용
1 - 모든 방 총 면적
2 - 침실 총 면적
3 - 비용(총 면적 - 줄인 값(발코니 면적 / 2)과 1평당 비용 곱하기)
'''

import sys
n, c = map(str, sys.stdin.readline().split())
info = {}
info["num"] = 0
info["bathroom"] = 0
info["balcony"] = 0
info["cost"] = 0

for _ in range(int(n)):
  num, type = map(str, sys.stdin.readline().split())
  info["num"] += int(num)
  
  if type == "balcony": 
    info["balcony"] += int(num)
  elif type == "bathroom": 
    info["bathroom"] += int(num)
    
  info["cost"] += int(num) * int(c)

for x in info:
  if x == "cost":
    print((info["num"] - (info["balcony"] / 2)) * int(c) , sep="\n")
  else:
    print(info[x], sep="\n")


#2 : 통과
'''
calculating different kinds of statistics for flats the agency

Reduced total area is the total area of all rooms except for balconies plus one half of balconies total area.

n - 방의 개수, c - 1평당 비용
1 - 모든 방 총 면적
2 - 침실 총 면적
3 - 비용(총 면적 - 줄인 값(발코니 면적 / 2)과 1평당 비용 곱하기)
'''

import sys
n, c = map(str, sys.stdin.readline().split())
info = {}
info["num"] = 0
info["bedroom"] = 0
info["balcony"] = 0
info["cost"] = 0

for _ in range(int(n)):
  num, type = map(str, sys.stdin.readline().split())
  info["num"] += int(num)
  
  if type == "balcony": 
    info["balcony"] += int(num)
  elif type == "bedroom": 
    info["bedroom"] += int(num)
    
  info["cost"] += int(num) * int(c)

for x in info:
  if x == "cost":
    print((info["num"] - (info["balcony"] / 2)) * int(c) , sep="\n")
  elif x == "bedroom" or x == "num" or x == "cost":
    print(info[x], sep="\n")