# 첫시도: 틀림
import sys
n, c = map(int, sys.stdin.readline().split())
arr = []
for _ in range(5):
  arr.append(int(sys.stdin.readline()))

arr.sort()
print((arr[0] + arr[-1]) // c)

# 두번째 시도:
'''
Q1.
"가장 인접한 두 공유기 사이의 거리를 가능한 크게 하여 설치하려고 한다." 
+ 
"C개의 공유기를 N개의 집에 적당히 설치해서, 가장 인접한 두 공유기 사이의 거리를 최대로 하는 프로그램을 작성하시오." 라고 하는데 

=> 공유기의 전파가 미치는 범위가 제시되어야 하는게 필요해보인다


Q2. 기준을 mid로 잡는 이유는?
'''