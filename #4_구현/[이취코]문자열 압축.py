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