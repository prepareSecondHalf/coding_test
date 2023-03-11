# 각 자리의 숫자(0~9)로만 이루어진 문자열 S가 주어졌을 때,
# 왼쪽 => 오른쪽 순으로 하나씩 모든 숫자를 확인하여 숫자 사이에 x 혹은 + 연산자를 넣어
# 가장 큰 결과를 나타내는 프로그램을 작성하시오
# 일반 사칙연산 방식이 아닌 왼쪽부터 순서대로 이루어지는 것을 가정한다.

# 첫째 줄에 여러 개의 숫자로 구성된 문자열 S가 주어진다.

# 첫째 줄에 가장 큰 정수를 출력한다.
import sys
s = list(map(int, sys.stdin.readline().strip()))
print(s)
# 풀이: 0은 곱하면 안되고 더해도 의미가 없으므로 무시한다.
# 1은 곱해도 의미가 없으므로 무조건 더한다.
# 나머지(2~9)는 무조건 곱하는게 커짐
sum = 0
for number in s:
    if number == 0:
        continue
    elif number == 1:
        sum += number
    else:
        if sum == 0:
            sum += number
        else:   
            sum *= number
print(sum)

# 이라고 생각했는데 s = 11111111111111111119같은 경우 안 됨