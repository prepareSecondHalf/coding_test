# n: 물품의 수 k: 버틸수 있는 무게
# 각 물건의 무게, 각 물건의 가치
# 출력: 무게가 k를 넘지 않을때 가치의 총합의 최댓값
import sys

n, k = map(int, sys.stdin.readline().split())
arr = []
d = [[0]*(k+1) for _ in range(n+1)]
dp = [0 for _ in range(n)]
for _ in range(n):
    arr.append(list(map(int, sys.stdin.readline().split())))
for i in range(1, n+1): # 1 ~ 물품의수
    for j in range(1, k+1): # 1 ~ 최대무게
        w = arr[i-1][0] #무게
        v = arr[i-1][1] #가치

        if j < w:
            d[i][j] = d[i-1][j]
        else:
            d[i][j] = max(d[i-1][j], d[i-1][j-w]+v)

print(d[n][k])