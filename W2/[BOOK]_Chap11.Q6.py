import numpy

# ft = [3, 1, 2]
ft = [2, 1, 2, 1, 6, 7]
k = 18

idx = 0
lastIndex = 0

while(True):
  if ft[idx] != 0: 
    k -= 1
    ft[idx] -= 1

  if ft.count(0) == len(ft) and k > 0:
    lastIndex = -1
    break

  if k == 0: 
    lastIndex = min(numpy.nonzero(ft))[0]
    break
  if lastIndex < 0: 
    lastIndex = -1 
    break
    
  if idx+1 == len(ft): idx = 0
  else: idx += 1
    
print(lastIndex)