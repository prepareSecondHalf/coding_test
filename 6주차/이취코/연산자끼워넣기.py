# 백준 14888
# n: 수의 개수
# n개의 수열
# a b c d (덧셈, 뺄셈, 곱셈, 나눗셈)개수
# 출력
# 첫번째줄: 만들수 있는식의 최댓값
# 두번째줄: 만들수 있는식의 최솟값

import sys

N = int(sys.stdin.readline())
num = list(map(int, sys.stdin.readline().split()))
op = list(map(int, sys.stdin.readline().split()))  # +, -, *, //

maximum = -1e9 # -10억
minimum = 1e9 # 10억


def dfs(depth, total, plus, minus, multiply, divide):
    global maximum, minimum
    # 재귀함수 반복후 depth == N이 되면 최댓값, 최솟값 뽑기
    if depth == N:
        maximum = max(total, maximum)
        minimum = min(total, minimum)
        return

    # 각 연산자를 끼워 넣어서 해당연산자로 계산, 해당 연산자 개수 -1 해서 재귀함수 실행
    if plus:
        dfs(depth + 1, total + num[depth], plus - 1, minus, multiply, divide)
    if minus:
        dfs(depth + 1, total - num[depth], plus, minus - 1, multiply, divide)
    if multiply:
        dfs(depth + 1, total * num[depth], plus, minus, multiply - 1, divide)
    if divide:
        dfs(depth + 1, int(total / num[depth]), plus, minus, multiply, divide - 1)


dfs(1, num[0], op[0], op[1], op[2], op[3])
print(maximum)
print(minimum)