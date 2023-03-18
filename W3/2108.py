import sys
from collections import Counter

n = int(sys.stdin.readline())
arr = []

for i in range(n):
    arr.append(int(sys.stdin.readline()))

arr = sorted(arr)

print(round(sum(arr)/n))
print(arr[int(len(arr)/2)])

counterCommon = Counter(arr).most_common()
common = 0

if len(counterCommon) == 1:
    common = counterCommon[0][0]
elif counterCommon[0][1] == counterCommon[1][1]:
    common = counterCommon[1][0]
else:
    common = counterCommon[0][0]
  
print(common)
print(int(max(arr) - min(arr)))