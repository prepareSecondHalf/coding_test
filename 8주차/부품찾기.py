# n: 가지고있는 부품의 개수
# 가지고 있는 부품 번호
# m: 확인해야하는 부품의 개수
# 확인 해야하는 부품 번호
import sys

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
b = list(map(int, sys.stdin.readline().split()))

for i in b:
    if i in a:
        print('yes', end=' ')
    else:
        print('no', end=' ')