# n: 원소 개수 k: 최대 바꿔치기 갯수
# 배열 A
# 배열 B
import sys

n, k = map(int, sys.stdin.readline().split())

a = list(map(int, sys.stdin.readline().split()))
b = list(map(int, sys.stdin.readline().split()))

a.sort()
b.sort(reverse=True)
for i in range(k):
    if a[i] < b[i]:
        a[i] = b[i]

print(sum(a))
