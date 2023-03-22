'''
  n명 
  양의 정수 k
  k번째 사람 제거 (n명 사람 모두 제거될 때까지)
  input = (n, k)

  ex)
  7 3
  n = 7
  k = 3
  arr = [1, 2, 3, 4, 5, 6, 7]
  result = []

  arr = [1, 2, '', 4, 5, 6, 7]
  result = [3]

  arr = [4, 5, 6, 7, 1, 2]
  arr = [4, 5, '', 7, 1, 2]
  result = [3, 6]

  arr = [7, 1, 2, 4, 5]
  arr = [7. 1, '', 4, 5]
  result = [3, 6, 2]
  
  arr = [4, 5, 7, 1]
  arr = [4, 5, '', 1]
  result = [3, 6, 2, 7]
    
  arr = [1, 4, 5]
  arr = [1, 4, '']
  result = [3, 6, 2, 7, 5]

  arr = [1, 4]
  result = [3, 6, 2, 7, 5, 1, 4]
'''

'''첫번째 시도'''
import sys
n, k = sys.stdin.readline().split(' ')
n = int(n)
k = int(k)
arr = list([i for i in range(1, n + 1)])
result = []

while True:
  if len(arr) < k: break

  result.append(arr[k - 1])
  del arr[k - 1]
  print('del:  ', arr)
  
  temp1 = arr[k - 1:]
  temp2 = arr[:k - 1]
  print('temp1:  ', arr[k - 1:])
  print('temp2:  ', arr[:k - 1])
  
  arr = temp1 + temp2
  print('arr:  ', arr)
  print('result: ', result, '\n')

result += arr
print('<', ', '.join(map(str, result)), '>', sep='')

'''두번째 시도'''
import sys
n, k = map(int, sys.stdin.readline().split(' '))
arr = list([i for i in range(1, n + 1)])
temp = []
index = 0

while arr:
  index += k - 1
#   print('index: ', index)
#   print('arr: ', len(arr), arr)
#   print('calc1: ', index % len(arr))
  
  if index >= len(arr):
    index %= len(arr)

  temp.append(str(arr.pop(index)))
#   print(temp, '\n')

print("<", ", ".join(temp), ">", sep="")