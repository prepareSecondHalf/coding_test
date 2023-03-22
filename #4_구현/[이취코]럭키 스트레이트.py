'''
  n 값
  반으로 나누었을 때,
  좌우 합이 동일할 때
  럭키스트레이트 스킬 사용 가능
  => 이 기술을 사용 가능한 상태인지 출력
  사용 가능 > LUCKY
  사용 불가 > READY
'''
import sys
input = sys.stdin.readline()
len = len(input)
mid = int(len/2)
left = str(input[0:mid])
right = str(input[mid:-1])

leftSum = 0
rightSum = 0

for i in left:
  leftSum += int(i)
for i in right:
  rightSum += int(i)

print('LUCKY' if leftSum == rightSum else 'READY')