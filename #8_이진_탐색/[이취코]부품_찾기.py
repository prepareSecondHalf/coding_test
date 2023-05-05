# 이진 탐색 : 재귀함수
# M개 종류의 부품 확인하여 가게 안에 모두 있는지 확인하는 프로그램
# 있으면 yes, 없으면 no

def binary_search(target, array, start, end):
  if start > end:
    return None
  mid = (start + end) // 2
  if array[mid] == target:
    return mid
  elif array[mid] > target:
    return binary_search(target, array, start, mid - 1)
  else:
    return binary_search(target, array, mid + 1, end)

import sys
N = int(sys.stdin.readline())
houseItems = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
requestItems = list(map(int, sys.stdin.readline().split()))

for idx in range(0, M):
  target = requestItems[idx]
  result = binary_search(target, houseItems, 0, N - 1)

  if result == None:
      print("no", end=" ")
  else:
      print("yes", end=" ")
  




# 이진 탐색 : 반복문
# M개 종류의 부품 확인하여 가게 안에 모두 있는지 확인하는 프로그램
# 있으면 yes, 없으면 no
def binary_search(target, array, start, end):
  while start <= end:
    mid = (start + end) // 2
    # print(target, array, start, end)
    if array[mid] == target:
      return mid
    elif array[mid] > target:
      end = mid - 1
    else:
      start = mid + 1
  return None

import sys
N = int(sys.stdin.readline())
houseItems = list(map(int, sys.stdin.readline().split()))
houseItems.sort()

M = int(sys.stdin.readline())
requestItems = list(map(int, sys.stdin.readline().split()))

for target in requestItems:
  result = binary_search(target, houseItems, 0, N - 1)
  if result == None:
        print("no", end=" ")
  else:
      print("yes", end=" ")
  


# 이진 탐색 : 계수정렬
# M개 종류의 부품 확인하여 가게 안에 모두 있는지 확인하는 프로그램
# 있으면 yes, 없으면 no

import sys
N = int(sys.stdin.readline())
houseItems = [0] * 1000001

for i in sys.stdin.readline().split():
  houseItems[int(i)] = 1

M = int(sys.stdin.readline())
requestItems = list(map(int, sys.stdin.readline().split()))

for target in requestItems:
  if houseItems[target] == 0:
        print("no", end=" ")
  else:
      print("yes", end=" ")
  


# 이진 탐색 : 집합 자료형
# M개 종류의 부품 확인하여 가게 안에 모두 있는지 확인하는 프로그램
# 있으면 yes, 없으면 no

import sys
N = int(sys.stdin.readline())
houseItems = set(map(int, sys.stdin.readline().split()))

M = int(sys.stdin.readline())
requestItems = list(map(int, sys.stdin.readline().split()))

for target in requestItems:
  if target in houseItems:
      print("yes", end=" ")
  else:
        print("no", end=" ")
  
