'''
    문자 1개부터 문자 길이만큼 순을 기준으로 하여
    압축을 하여 압축된 길이를 배열에 담아 그 중 가장 짧은 요소 길이를 반환
'''
'''첫번째 시도'''
import sys
input = sys.stdin.readline()

idx = 1
arr = []
for i in range(idx):
  target = input[:idx]
  print('target: ', target)
  cnt = 0
  temp = ''
  
  for j in range(len(input)):
      if input[j] != target:
        if cnt != 1: 
          temp = str(cnt) + input[j - 1]
        else:
          temp = input[j - 1]
        arr.append(temp)
        cnt = 1
        target = input[j]
      elif input[j] == target:
        cnt += 1
      print('j:  ', j, 'cnt:  ', cnt)
  print('temp:', temp)

print(arr)

''' 두번째 시도'''
'''
  ex1) aabbaccc
  문자열 길이만큼 탐색
    > n은 1부터 문자열 길이만큼 증가
  
  첫번째 요소를 타겟 + n개 길이를 기준
  > 기준이 되는 요소값이 다른 요소값을 만나기 전 분기 처리 
    > 몇 개 요소가 같은지 카운팅 > 갯수와 해당요소를 합한다 > 준비한 배열에 추가한다
  > 기준이 되는 요소값이 다른 요소값이 없다면 > 갯수를 제외한 문자열만 준비한 배열에 추가한다
  
  > 다만, 제일 앞부터 정해진 길이만큼 잘라야 함
  탐색 한 바퀴가 종료
  > 배열에 추가한 값들을 모두 합친다 > 해당 길이를 준비한 길이값을 모아두는 배열에 추가한다

  두번째 인덱스까지의 요소 타겟 + 2개 길이 기준
  > ...

  최종
  > 해당 길이값이 있는 배열에서 가장 최소값을 반환한다
    
'''

import sys
input = sys.stdin.readline()

idx = 1
arr = []
lenArr = []

while idx <= len(input):
  for i in range(0, len(input), idx):
    target = input[:idx]
    
    print('lenArr:  ', lenArr)
    print('target: ', target)
    print('arr: ', arr)
    cnt = 0
    temp = ''
    if (len(arr) > 1):
      sum = ''
      for x in arr:
        sum += x
      
    arr = []
    
    for j in range(0, len(input) - 1, idx):
        print('input[:j]:  ', input[:idx], ' \n')
                
        if input[j] == target:
          cnt += 1
          print('@@@@@cnt++ moment!', cnt)
          
        if target != input[j]:
          print('@@@@@checkIt moment!', input[:idx], input[j])
          if cnt > 1:
            temp = str(cnt) + input[j - 1]
          else:
            temp = input[j]
          
          print('j:  ', j, 'cnt:  ', cnt, 'target:  ', target, 'el:  ', input[:j], 'temp:  ', temp)
          arr.append(temp)
          cnt = 1
          target = input[j]
          temp = ''

        print('arr', arr)
    print('temp:', temp, '\n\n\n')
    lenArr.append([temp, len(temp)])
    idx += 1


''' 예제 코드 '''
def solution(s):
  answer = len(s)

  # 1개 단위(step)부터 압축 단위를 늘려가며 확인
  for step in range(1, len(s) // 2 + 1):
    compressed = ''
    prev = s[0:step] # 앞에서부터 step만큼 문자열 추출
    count = 1

    # 단위(step) 크기만큼 증가시키며 이전 문자열과 비교
    for j in range(step, len(s), step):
      # 이전 상태와 동일하다면, 압축 횟수(count) 증가
      if prev == s[j:j + step]:
        count += 1
      # 다른 문자열이 나왔다면(더 이상 압축하지 못하는 경우라면)
      else:
        compressed += str(count) + prev if count >= 2 else prev
        prev = s[j:j + step] # 다시 상태 초기화
        count = 1
    
    # 남아 있는 문자열에 대해서 처리
    compressed += str(count) + prev if count >= 2 else prev

    # 만들어지는 압축 문자열이 가장 짧은 것이 정답
    answer = min(answer, len(compressed))
  return answer