import sys
import math
t = int(sys.stdin.readline())
first = 0
second = 0
third = 0
if t % 10 != 0:
    print(-1)
else:
    first = int(math.trunc(t / 300))
    second = int(math.trunc((t-first*300) / 60))
    third = int(math.trunc((t-first*300-second*60) / 10))
    print(first, second, third)