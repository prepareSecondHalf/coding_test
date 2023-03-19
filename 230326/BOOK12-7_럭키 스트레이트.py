# 게임의 아웃복서 캐릭터는 '럭키 스트레이트' 필살기가 있다. 매우 강력하나 점수가 특정 조건일 때만 사용 가능하다.
# 현재 점수가 N일 때, 자릿수를 기준으로 N을 반으로 나누어 왼쪽 부분의 각 자릿수의 합과 오른쪽 부분의 각 자릿수의 합이 동일한 상황이다.
# 현재 점수 N이 주어질 때, 기술을 사용할 수 있는 상태인지 아닌지를 알려주는 프로그램을 작성하시오

# 첫째 줄이 정수 N이 항상 짝수 개의 자릿수의 형태로 주어진다. (10 <= N <= 99,999,999)

# 첫째 줄에 럭키 스트레이트를 사용할 수 있는지 여부를 "LUCKY" 또는 "READY"로 출력한다.

# 풀이: 문자열 상태에서 나눠야 하므로 굳이 int로 안 바꾸고 받는 걸로... 그냥 시키는대로 하면 된다.
import sys
n = sys.stdin.readline().strip()
center_idx = len(n) // 2
left_part = list(map(int, n[:center_idx]))
right_part = list(map(int, n[center_idx:]))
if sum(left_part) == sum(right_part):
    print('LUCKY')
else:
    print('READY')