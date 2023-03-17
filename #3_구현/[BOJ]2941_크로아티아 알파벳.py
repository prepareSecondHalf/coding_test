'''
  보기 요소 배열을 만든다
  보기 요소를 탐색하면서 입력값에 해당하는 값이 있는지 확인한다
  있을 경우, 보기에서 제거 후 카운팅

  보기 요소 한 바퀴 돌았을 경우,
  남아있는 요소 갯수와 기존 카운팅을 합하여 반환한다
'''

''' 실패 코드 '''
li = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
input = input()
cnt = 0

for t in li:
  x = input.find(t)
  print('\n\n', t)
  print(x)
  print(input)
  
  if x > -1:
    input = input.replace(t, '')  
    print(input)
    cnt += 1

print(cnt)
print(len(input) + cnt)


''' 성공 코드 '''
li = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
input = input()

for t in li:
    input = input.replace(t, '*')  

print(len(input) )