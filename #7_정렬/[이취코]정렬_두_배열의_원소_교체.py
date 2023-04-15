'''
  두 개의 배열
  - n개의 원소로 구성
  - 자연수임
  k번 바꿔치기 연산 수행 가능
  - 배열 a의 원소와 배열 b의 원소 하나씩 교환

  배열 a의 원소 합 최대가 목표

  수도코드
  첫 입력값을 n과 k로 정의
  2번의 for문으로 배열 a와 배열 b를 정의

  for i in range(int(k)):
    minA = 배열 a의 최솟값을 구한다
    maxB = 배열 b의 최댓값을 구한다
    minA, maxB를 스와핑한다

  result = 배열 a의 sum을 구한다
  print(result)
'''

import sys
n, k = input().split()

# for _ in range(int(n)): 흠.. 이러면 받은 값을 저장해주는 또다른 배열을 만들어줘하는 번거로움 발생!!
A = list(map(int, sys.stdin.readline().split()))
B = list(map(int, sys.stdin.readline().split()))
print(A, B)

for _ in range(int(k)):
  minA = min(A)
  maxB = max(B)

  idxMinA = A.index(minA)
  idxMaxB = B.index(maxB)

  A[idxMinA], B[idxMaxB] = B[idxMaxB], A[idxMinA]

# print(A, B)
# result = [sum += x for x in range(len(A))] -> list comprehension is tool of input, not a calculation(or arithmatic operation)

print(A)

from functools import reduce
# from operator import mul
sum = reduce(lambda acc, cur: acc + cur, A, 0)
print(sum)

# 출처
# https://stackoverflow.com/questions/16632124/how-to-emulate-sum-using-a-list-comprehension
# https://www.daleseo.com/python-functools-reduce/