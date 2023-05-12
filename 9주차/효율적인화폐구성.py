# n: 화폐의 종류, m: 만들어야하는 금액
# n개의 화폐의 가치
# 출력: 최소한의 화폐개수(불가능할시 -1 출력)
# 주어진 화폐를 이용해 m을 만들수 있는 최소한의 화폐개수
import sys

n, m = map(int, sys.stdin.readline().split())
money = []
for _ in range(n):
    money.append(int(sys.stdin.readline()))

d = [10001] * (m + 1)
d[0] = 0
for i in range(n): # i = 각각의 화폐단위(money[i])
    for j in range(money[i], m+1): # j = 각각의 금액
        if d[j - money[i]] != 10001:
            d[j] = min(d[j], d[j-money[i]] + 1)

if d[m] == 10001:
    print(-1)
else:
    print(d[m])
