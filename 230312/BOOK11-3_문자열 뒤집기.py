# 다솜이는 0과 1로만 이루어진 문자열 S를 가지고 있습니다. 
# 문자열 S의 모든 숫자를 같게 하려고 합니다.
# 할 수 있는 행동은 연속된 하나 이상의 숫자를 잡고 모두 뒤집는 것(0 => 1, 1 => 0)입니다.
# 모든 숫자를 같게 할 수 있는 행동의 최소 횟수는?

# 첫째 줄에 0, 1로만 이루어진 S가 주어진다.

# 첫째 줄에 행동의 최소 횟수를 출력한다.
import sys
s = list(map(int, sys.stdin.readline().strip()))

# 숫자가 바뀌는 지점의 수를 체크하면 될 듯?
# 모두 연속된 숫자 => 바뀌는 지점 0, 뒤집는 행동 0
# 001100 => 바뀌는 지점 2, 뒤집는 행동 1
# 00110011 => 바뀌는 지점 3, 뒤집는 행동 2
# 010010 => 바뀌는 지점4, 뒤집는 행동 2
# 0100101 => 바뀌는 지점5, 뒤집는 행동 3
# ...
# 바뀌는 지점이 홀수 개일 때는 0 또는 1이 연속되는 횟수가 동일하다는 의미 => 어느 쪽이든 출현 횟수(연속)
# 바뀌는 지점이 짝수 개일 때는 더 적은 쪽을 뒤집으면 됨 => 적은 쪽의 출현 횟수(연속)

prev_number = s[0]
turn_point = 0
for number in s[1:]:
    if prev_number != number:
        turn_point += 1
    prev_number = number
if prev_number % 2 == 0:
    print(turn_point // 2)
else:
    print(turn_point // 2 + 1)