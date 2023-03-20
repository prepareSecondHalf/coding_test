'''
  공집합 s가 주어짐
  주어지는 값: x일 수도 있고 아닐 수 있음
  x는 1 이상 20 이하
  
  add: s에 x가 없을 경우 추가, 있으면 무시
  remove: s에 x가 없을 경우 무시, 있으면 제거
  check: s에 x가 있을 경우 1 출력, 없으면 0 출력
  toggle: s에 x가 있으면 x 제거, 없으면 추가
  all: s를 {...} 으로 바꿈
  empty: s를 공집합으로 바꿈
'''

''' 첫번째 시도'''
import sys

m = int(input())
s = set()
for i in range(m):
  # type, num = list(input().split(' '))
  input = list(sys.stdin.readline().split(' '))
  input[1] = int(input[1])
  
  if (input[0] == 'add' and input[1] in s == True and input[1] >= 1 and input[1] <= 20): s.add(input[1])
  elif (input[0] == 'check'):
    if (input[0] == 'check' and input[1] in s == True and input[1] >= 1 and input[1] <= 20): print(1)
    else: print(0)
  elif (input[0] == 'remove'):
    if (input[0] == 'remove' and input[1] in s == True and input[1] >= 1 and input[1] <= 20): s.remove(input[1])
  elif (input[0] == 'toggle'):
    if (input[0] == 'toggle' and input[1] in s == True and input[1] >= 1 and input[1] <= 20): s.remove(input[1])
    else: s.add(input[1])
  elif (input[0] == 'empty'):
    s.clear()
  elif (input[0] == 'all'):
    s = set([i for i in range(1, 21)])
    
print(s)