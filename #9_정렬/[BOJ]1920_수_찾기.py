# 첫 시도 : 시간 초과
import sys
n = sys.stdin.readline()
nArr = list(map(int, sys.stdin.readline().split()))
m = sys.stdin.readline()
mArr = list(map(int, sys.stdin.readline().split()))

for target in mArr:
  try:
    if nArr.index(target) > 0:
      print(1)
  except:
    print(0)

# 두번째 시도 : 시간 초과
import sys
n = sys.stdin.readline()
nArr = set(map(int, sys.stdin.readline().split()))
m = sys.stdin.readline()
mArr = list(map(int, sys.stdin.readline().split()))

for target in mArr:
  print(1) if target in nArr else print(0)



# 세번째 시도
import sys
n = sys.stdin.readline()
nArr = set(map(int, sys.stdin.readline().split()))
m = sys.stdin.readline()
mArr = list(map(int, sys.stdin.readline().split()))

for target in mArr:
  print(1) if target in nArr else print(0)


# 네번째 시도: 통과
import sys
n = int(sys.stdin.readline())
nArr = list(map(int, sys.stdin.readline().split()))
nArr.sort()
m = sys.stdin.readline()
mArr = list(map(int, sys.stdin.readline().split()))

for target in mArr:
  start, end = 0, n - 1
  isExist = False
  
  while start <= end:
    mid = (start + end) // 2
    if nArr[mid] == target:
      isExist = True
      print(1)
      break
    elif nArr[mid] > target:
      end = mid - 1
    else:
      start = mid + 1
  if isExist == False:
    print(0)
  
