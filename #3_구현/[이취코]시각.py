'''
  정수 N은 시간
  00시 00분 00초부터 N시 59분 59초까지 범위 중 3이 포함된 
  시각의 갯수를 센다

  000000부터 N0000까지 1씩 추가하여 3이 발견할 때마다 카운트한다
'''

t = int(input())
h = 0
m = 0
s = 0

def clock():
  global h
  global m
  global s

  if s == 60:
    s = 0
    m += 1
    if m == 60:
      m = 0
      h += 1
  elif m == 60:
    m = 0
    h += 1


cnt = 0
while True:
  clock()
  print('h: ', h, ' m: ', m, ' s: ', s)
  
  if (str(h).find('3') != -1 or str(m).find(3) != -1 or str(s).find(3) != -1): cnt += 1
  if (h == t and m == 59 and s == 59):
    break;

print(cnt)

'''예제코드'''
h = int(input())
cnt = 0
for i in range(h + 1):
  for j in range(60):
    for k in range(60):
      if '3' in str(i) + str(j) + str(k):
        cnt += 1

print(cnt)