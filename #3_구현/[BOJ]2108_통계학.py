'''
  avg
  mid
  view
  range

  오름차순 정렬
  평균을 구한다(전체합 / 개수)
  중앙값을 구한다(범위/2)
  가장 큰 값을 구한다(max)
  범위를 구한다(cnt)
'''

''' 실패 코드 '''
from collections import Counter
n = int(input())
arr = []
for x in range(n):
  num = int(input())
  arr.append(num)

# print(arr)

arr = sorted(arr, reverse=False)
# print(arr)
counter = Counter(arr)
most = counter.most_common(2)
# print(most)

if (n > 1):
  first = most[0][1]
  second = most[1][1]
  
  if (first == second): maximum = most[1][0]
  else: maximum = most[0][0]
else:
  maximum = most[0][0]
# print(first)
# print(second)


sum = sum(arr)
print(sum)
print('avg: ', round(sum/n))
print('mid: ', arr[round(n / 2)])
print('view: ', maximum)
print('range: ', arr[n - 1] - arr[0])



''' 아직 성공 코드(왜 통과가 안 될까요? ㅠ) '''
from collections import Counter
import sys

#n = int(input())
n = int(sys.stdin.readline())
arr = []

for _ in range(n):
    num = int(int(sys.stdin.readline()))
    arr.append(num)

arr = sorted(arr, reverse=False)
counter = Counter(arr)
most = counter.most_common(2)
first = most[0][1]
second = most[1][1]

if (len(most) > 1 and first == second ):
    maximum = most[1][0]
else:
    maximum = most[0][0]

print(round(sum(arr)/n))
print(arr[round(n / 2)])
print(maximum)
# print(arr[n - 1] - arr[0])
print(max(arr) - min(arr))



''' 성공 코드 '''