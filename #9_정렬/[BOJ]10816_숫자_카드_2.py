# 첫 시도
# n개 카드
# m이 주어졌을 때, m이 있는 숫자카드를 상근이가 몇 개 소유하고 있는지 구하기
def binary_search(array, target, start, end, count):
  print('count:  ', count, start, end)
  
  if start > end:
      return count
    
  mid = (start + end) // 2
  print('mid:  ', mid)
  if array[mid] > target:
    end = mid - 1
    return binary_search(array, target, start, end, count)
  elif array[mid] < target:
    start = mid + 1
    return binary_search(array, target, start, end, count)
  else:
    print('check!!!!!!!!!!!!!!!!!!', mid, target, count)
    if array[mid - 1] == target: 
      return binary_search(array, target, 0, mid - 1, count + 1)
    elif array[mid - 1] == target: 
      return binary_search(array, target, mid + 1, end, count + 1)
    
    

import sys
n = int(sys.stdin.readline())
allCards = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
allCards.sort()
targetCards = list(map(int, sys.stdin.readline().split()))
# targetCards.sort()
# print('targetCards: ', targetCards)
print('allCards: ', allCards)

results = {}
for target in targetCards:
  count = 0
  results[target] = count
  result = binary_search(allCards, target, 0, n - 1, count)
  print('result: ', result)
  
  results[target] += result
  print('results: ', results, '\n\n')

print('final results: ', results)
for x in targetCards:
  print(results[x], end=" ")

# 두번째 시도
# n개 카드
# m이 주어졌을 때, m이 있는 숫자카드를 상근이가 몇 개 소유하고 있는지 구하기
def binary_search(array, target, start, end):
  if start > end:
      return 0
  mid = (start + end) // 2
  if array[mid] > target:
    end = mid - 1
    return binary_search(array, target, start, end)
  elif array[mid] < target:
    start = mid + 1
    return binary_search(array, target, start, end)
  else:
    return results.get(target)    
    

import sys
n = int(sys.stdin.readline())
allCards = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
allCards.sort()
targetCards = list(map(int, sys.stdin.readline().split()))

results = {}
for target in allCards:
  if target in results:
    results[target] += 1
  else:
    results[target] = 1

for target in targetCards:
  print(binary_search(allCards, target, 0, n - 1), end=" ")


# 다른 코드

import sys
n = int(sys.stdin.readline())
allCards = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
allCards.sort()
targetCards = list(map(int, sys.stdin.readline().split()))

results = {}
for target in allCards:
  if target in results:
    results[target] += 1
  else:
    results[target] = 1

for target in targetCards:
  if target in results:
    print(result[target], end=" ")
  else:
    print(0, end=" ")