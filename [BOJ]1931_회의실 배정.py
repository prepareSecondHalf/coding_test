# !!!!!!!!Attribute Error!!!!!!!!!! : 원인이 무엇일까요??.......
import sys
input = sys.stdin.readline
cnt = 0
def list_chunk(lst, n):
  return [lst[i:i+n] for i in range(0, len(lst), n)]
  
N = (list(map(int, input.split())))[0]
input = (list(map(int, input.split())))[1:]
input = list_chunk(input, 2)
input.sort(key=lambda x:(x[0], x[1]))

if len(input) == 1:
  print(1)
else:
  tryCnt = []
  arr = []
  
  for y in input:
    start = y[0]
    end = y[1]
    arr.append(y)
    
    for x in input:
      if (end <= x[0] and x[0] != x[1]):
        start = x[0]
        end = x[1]
        arr.append(x)
    tryCnt.append(len(arr))
    arr = []
    
  print(max(tryCnt))
  