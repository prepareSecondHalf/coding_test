'''
  k개의 정수
  '0' 등장 시, 최근 나온 수를 지운다
  아닐 경우, 해당 수를 배열에 추가
  최종 남은 배열 요소의 합을 산출
  ex1)
  k = 4
  [4, 3]
  [4]
  []
  => 0
'''

k = input()
arr = []
for i in range(int(k)):
  integer = int(input())
  if integer != 0:
    arr.append(integer)
  else: arr.pop()

print(sum(arr))