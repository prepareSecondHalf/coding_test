import sys

case = int(sys.stdin.readline())

for i in range(case):
  n, m = map(int, sys.stdin.readline().split())
  doc = list(map(int, sys.stdin.readline().split()))
  
  idxArr = [0] * n
  idxArr[m] = 1
  cnt = 0
  
  while True:
    if doc[0] == max(doc):
      cnt += 1
      if idxArr[0] != 0:
        print(cnt)
        break
      else:
        doc.pop(0)
        idxArr.pop(0)
    else:
      doc.append(doc.pop(0))
      idxArr.append(idxArr.pop(0))