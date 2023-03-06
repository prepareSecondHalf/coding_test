# 양수, +, -, 괄호로 식을 만들었다. 이후 괄호를 모두 지우고 다시 괄호를 추가해 식의 값을 최소로 만들려고 한다.

# 첫째 줄에 식이 주어진다. 식은 0~9, +, -로만 이루어져 있고, 가장 처음과 마지막은 숫자이다. 연속해서 두 개의 연산자가 나타나지 않고, 5자리보다 많이 연속되는 숫자는 없으며 숫자는 0으로 시작할 수 있다. 식의 길이는 50 이하이다.

# 첫째 줄에 정답을 출력한다.


import sys
expression = sys.stdin.readline().strip()
# 풀이
# 덧셈은 괄호를 붙여도 똑같다.
# 뺄셈은 -1이 곱해진 것과 같으므로 괄호 여부에 따라 값이 달라질 수 있다.
# A - B + C => A - (B + C) => 결과가 작아지므로 o
# A - B - C => A - (B - C) => 결과가 커지므로 x => A - B - C
# 즉 -를 기준으로 식을 split하고, 각각의 식(+)을 계산 => 빼면 됨
splitted = expression.split('-')
result = 0
for idx, val in enumerate(splitted):
    minus_target = sum(list(map(int, val.split('+'))))
    if idx == 0:
        result += minus_target
    else:  
        result -= sum(list(map(int, val.split('+'))))
print(result)