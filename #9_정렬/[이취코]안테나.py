# 시간초과!!!!!!!!!

import sys
n = int(sys.stdin.readline())
array = list(map(int, sys.stdin.readline().split()))
array.sort()

totalArr = []
for t in array:
  total = 0
  for tt in array:
    total += abs(tt - t)
  totalArr.append(total)

min = min(totalArr)
for idx in range(0, len(totalArr)):
  if totalArr[idx] == min: 
    print(array[idx])
    break

'''
처음 문제를 보고 모든 값 집의 위치 마다 거리를 계산 했다.
이 경우 n^2의 시간 복잡도를 가지는데 입력값의 최대가 200,000이라서 무조건 시간 초과가 나오게 된다.
'''


# 참고 코드
import sys
n = int(sys.stdin.readline())
array = list(map(int, sys.stdin.readline().split()))
array.sort()
print(array[(n - 1) // 2])
'''
n에 1를 빼는 이유는
홀수일 때는 어차피 나머지가 1이므로 값이 같고, 
짝수일 때 그냥 2로 나누면 오른쪽에 위치한 집의 값이 나온다.
(6을 2로 나누면 3이니까) 
따라서 다음에 -1을 해줘야 하는데 
이러면 홀수일 때를 따로 또 분리해 줘야 하므로 
애초에 크기보다 1 작은 값을 2로 나누면 해결되는 아이디어다.
'''


'''
수학적으로 생각하면 간단하게 풀 수 있는 문제이다.
모든 집까지의 거리의 총합이 가장 작으려면 일직선 상에서 가운데에 가까울 수록 총합이 적어진다.
그래서 배열에 집의 위치를 저장하고 정렬 후 중앙값을 찾아서 출력하면 된다.
'''