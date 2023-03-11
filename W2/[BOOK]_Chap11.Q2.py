n = '5555123555555555555'

list = list()
res = ''
cnt = 0
plusCnt = 0

for i in range(len(n)):
  if int(n[i]) == 0: plusCnt += 1
  list.append(n[i])

list.sort()

while cnt < len(list):
  for i in list[:plusCnt]:
    res += '+' + i
    
    cnt += 1

  for i in list[plusCnt:]:
    if cnt == plusCnt: res += '+' + i
    else: res += '*' + i
    
    cnt += 1

  if int(eval(res)) >= 2000000000: 
    cnt = 0
    plusCnt += 1
    res = ''

print(eval(res))