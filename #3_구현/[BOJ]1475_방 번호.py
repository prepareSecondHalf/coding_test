'''
한 세트당 0~9까지 숫자가 존재
6과 9는 상호보완 관계
입력값을 만족하기 위한 최소 필요 세트 수 구하기

입력값 길이를 구한다

반복
[인덱스를 이용하여 입력값에 접근
인덱스 값이 세트에 존재하면 통과
인덱스 값이 세트에 존재하지 않을 경우 새로운 세트 추가]

사용한 세트 수 출력
'''

''' 실패 코드 '''
global cnt
global numSet
global existedSix
global existedNine

n = '9999'
cnt = 1
numSet = ''.join([str(x) for x in range(0, 10)])

existedSix = -1
existedNine = -1

def delSixNine():
  print('check #1')
  
  global existedSix
  global existedNine
  global numSet

  existedSix = numSet.find('6')
  existedNine = numSet.find('9')
  
  print('existedSix:  ', existedSix)
  print('existedNine:  ', existedNine)
  
  if existedSix > -1 : numSet.strip('6')
  elif existedSix == -1 and existedNine > -1 : numSet.strip('9')
  elif existedSix > -1 and existedNine == -1 : numSet.strip('6')
  else: False
    
    
  print('numSet:  ', numSet, '\n')

def createNums():
    global cnt
    global numSet

    print('check #2')
    cnt += 1
    numSet = ''.join([str(x) for x in range(0, 10)])

# main
for target in n:
  targetIdx = numSet.find(target)
 
  if targetIdx > -1:
    if target == '6' or target == '9':
      if delSixNine() == False: 
        createNums()
        delSixNine()
      else: 
    else: 
      del numSet[targetIdx]
  else:
    createNums()
    print('check:  ', target)

    
print(cnt)
  
# def newNumSet():
#   numSet = [x for x in range(0, 10)]
#   print(numSet)

# newNumSet() 
# print(numSet) # Q. 빈 값이 왜 나올까요?


''' 성공 코드 '''
word = input()
ans = [0] * 10

for i in range(len(word)):
  num = int(word[i])

  if num == 6 or num == 9:
    if ans[6] <= ans[9]:
      ans[6] += 1
    else:
      ans[9] += 1
  else:
    ans[num] += 1

print(max(ans))
