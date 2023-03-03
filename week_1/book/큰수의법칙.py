import sys

n, m, k = map(int, sys.stdin.readline().strip().split())
data = list(map(int, sys.stdin.readline().strip().split()))

data.sort()

maxVal = data[n - 1]
secondMaxVal = data[n - 2]

maxCnt = m // k * k
maxCnt += (m % k) % (m // k)

result = maxVal * maxCnt + secondMaxVal * (m - maxCnt)

print(result)