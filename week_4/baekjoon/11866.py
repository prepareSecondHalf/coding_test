import sys

N, K = map(int, sys.stdin.readline().strip().split())
arr = [x for x in range(1, N + 1)]

currentIdx = -1
horse = 0
result = []

def move(idx, datasLen):
    idx += 1

    if idx == datasLen:
        idx = 0

    return idx

while True:
    if len(arr) == 1:
        result.append(arr[0])
        break

    horse += 1
    currentIdx = move(currentIdx, len(arr))

    if horse == K:
        data = arr.pop(currentIdx)
        result.append(data)
        horse = 0
        currentIdx = -1

result = list(map(str, result))
result = ', '.join(result)
print('<' + result + '>')