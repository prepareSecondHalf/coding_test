import sys
n = sys.stdin.readline()
arr = []


for i in n:
  arr.append(i)

remove_set = { '6', '9' }
exArr = [i for i in arr if i not in remove_set]

maxCountNumber = max(arr, key = arr.count)
exArrCountNumber = max(exArr, key = arr.count)

num = 0

def mathRound(n):
  if (n - int(n)) >= 0.5:
    return int(n) + 1
  else:
    return int(n)

if maxCountNumber != exArrCountNumber: 
  if arr.count(maxCountNumber)/2 < exArr.count(exArrCountNumber):
    num = exArr.count(exArrCountNumber)
  else:
    if arr.count('9') == 0 or arr.count('6') == 0:
      num = mathRound(arr.count(maxCountNumber)/2)
    else:
      sum = (arr.count('9') + arr.count('6'))/2
      sum = mathRound(sum)
      num = sum
else:
  num = arr.count(maxCountNumber)
  
print(num)