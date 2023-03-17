'''
    수도 코드
'''
# 배열 요소를 탐색
# 각 요소를 인덱스별로 탐색 (loop)
  # 인덱스별 알파벳이 validCheck에 없으면, 
  # 추가 및 isConsecutive 값 true
  
  # 인덱스별 알파벳이 validCheck에 있는 경우
    # 이전 인덱스값이 동일 값이거나 다음 인덱스값이 동일값이면,   
      # isConsecutive 값 true
    # 이전 인덱스값과 다음 인덱스값이 상이하면,
      # isConsecutive 값 false
      # 다음 요소 탐색

# 다음 요소 탐색 전 isConsecutive 값이 true면 cnt 플러스1 추가 
# 배열 탐색 종료 후 cnt 값 출력

'''
    실패 코드
'''
import sys
# n, target = map(int, sys.stdin.readline().split())
int(N) = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
cnt = 0

for target in arr:
    validCheck = []
    
    for idx in range(len(target)):
        try: 
            if (validCheck.index(target[idx])): 
                if (target.find(target[idx]) == idx - 1 or target.find(target[idx]) == idx + 1): 
                    continue
                elif ( (target.find(target[idx]) > idx and (target.find(target[idx]) != idx - 1) or  (target.find(target[idx]) != idx + 1)) ):
                    cnt += 1
                    break;
        except ValueError:
            validCheck.append(target[idx])

print(n - cnt)




'''
    성공 코드
'''
input = sys.stdin.readline

n = int(input())

cnt = n
for i in range(n):
    d = input()

    for j in range(len(d)-1):
        if d[j] == d[j+1]:
            #  Q. 예를 들어, aabbb의 경우 마지막 a와 마지막 b는 검증을 어떻게 할 것인가?
            pass
        elif d[j] in d[j+1:]:
            cnt -= 1
            break

print(cnt)

