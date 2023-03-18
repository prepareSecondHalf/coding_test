import sys

datas = list(str(sys.stdin.readline()))
numCnt = [0] * 10

for data in datas:
    if int(data) == 9:
        numCnt[6] += 1
    else:
        numCnt[int(data)] += 1

if numCnt[6] % 2 == 0:
    numCnt[6] = numCnt[6] // 2
else:
    numCnt[6] = numCnt[6] // 2 + 1

print(max(numCnt))