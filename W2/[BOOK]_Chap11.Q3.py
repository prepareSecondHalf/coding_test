import sys

n = sys.stdin.readline()
lessNum = ''
cnt = 0
preStr = n[0]

for i in n:
  if i != preStr:
    cnt += 1

  preStr = i

print(int(cnt)//2) 