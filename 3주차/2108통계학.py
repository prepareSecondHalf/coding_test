import sys
import math
from collections import Counter

n = int(sys.stdin.readline())
number = []

for i in range(n):
    number.append(int(sys.stdin.readline().strip()))

number.sort()
a = round(sum(number) / n)
print(a)
b = number[math.floor(n / 2)]
print(b)

c = Counter(number).most_common()
if len(c) > 1:
    if c[0][1] == c[1][1]:
        print(c[1][0])
    else:
        print(c[0][0])
else:
    print(c[0][0])

d = number[n-1] - number[0]
print(d)
