import sys

a, b, c = 300, 60, 10

cntA, cntB, cntC = 0, 0, 0

time = int(sys.stdin.readline())

while time>=10:
  if time//a > 0:
    cntA += time//a
    time -= a * (time//a)
  elif time//b > 0:
    cntB += time//b
    time -= b * (time//b)
  elif time//c > 0:
    cntC += time//c
    time -= c * (time//c)

if time > 0: print(-1)
else: print(cntA, cntB, cntC)