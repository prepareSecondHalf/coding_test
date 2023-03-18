# 왼쪽위 =(1,1) 좌표는 (a, b) 1 <= a <= 8, 97 <= 좌표[1] <= 104
import sys

n = sys.stdin.readline()
steps = [(-2, 1), (-2, -1), (2, -1), (2, 1), (1, -2), (1, 2), (-1, 2), (-1, -2)]
a = ord(n[0])
b = int(n[1])
count = 0
for i in steps:
    if (a + i[0] <= 104 and a + i[0] >= 97) and (b + i[1] <= 8 and b + i[1] >= 1):
        count += 1

print(count)