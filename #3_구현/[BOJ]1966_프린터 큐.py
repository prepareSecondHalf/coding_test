'''
  테스트 갯수 3
  맨 왼쪽은 0번째
  N개 문서의 중요도가 차례대로 주어짐
  중요도는 1 이상 9 이하의 정수
  중요도가 같은 문서가 여러 개 있을 수도 있음
  나머지 문서들 중 현재 문서보다 중요도가 높은 문서가 하나라도 있다면, 이 문서를 인쇄하지 않고 Queue의 가장 뒤에 재배치 한다. 그렇지 않다면 바로 인쇄를 한다.
  
  #1
  문서 갯수 1
  몇 번째에 놓여 있는지를 나타내는 정수 0

  #2
  문서 갯수 4
  몇 번째에 놓여 있는지를 나타내는 정수 2
  

  [반복]
  {
    t = 중요도가 가장 높은 요소를 찾는다
    첫번째 요소의 중요도보다 뒤 요소가 중요도가 높다면, 
    t요소를 배열 추가
    
    t요소 다음 요소의 중요도보다 뒤 요소가 중요도가 높다면,
    해당 요소에 접근 후 배열 추가

    만약 뒤요소가 없지만 앞요소가 있다면, 맨 앞 요소로 이동

    if 관심있는 요소의 순번이 왔을 경우, 해당 순번을 리턴
  }
'''
# input = '''
# 3
# 1 0
# 5
# 4 2
# 1 2 3 4
# 6 0
# 1 1 9 1 1 1'''

''' 실패 코드 '''
n = 4
idx = 2
nums = '1 2 3 4'
numsArr = nums.split(' ')
nums = nums.replace(' ', '')
len = len(nums)
result = []

for y in range(n):
  maxNum = (max(nums))
  maxIdx = nums.find(maxNum)
  result.append(nums[maxIdx])

  print(numsArr, maxIdx)
  print(numsArr[maxIdx])
  
  del numsArr[maxIdx]
  print(numsArr)
  print('\n')
  


''' 성공 코드 '''
t = int(input())
for i in range(t):
    n, m = map(int, input().split())
    s = list(map(int, input().split()))
    s_ = [0 for i in range(n)]
    s_[m] = 1
    cnt = 0
    while True:
        if s[0] == max(s):
            cnt += 1
            if s_[0] == 1:
                print(cnt)
                break
            else:
                del s[0]
                del s_[0]
        else:
            s.append(s[0])
            del s[0]
            s_.append(s_[0])
            del s_[0]

'''
중요도를 리스트에 담아준다음, 위치를 저장할 리스트도 만들어 준다.
차례대로 검사를 해주면서 제일 큰 값이면 cnt에 1을 더해주고 삭제,
아니라면 맨 뒤에 넣어주고 삭제를 해가고,
만약 제일 큰 값을 찾았고, 그 값이 내가 찾을 숫자이면 break해주고 cnt를 출력해준다.
'''