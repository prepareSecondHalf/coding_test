# 숫자 카드 게임은 여러 개의 숫자 카드 중에서 가장 높은 숫자가 쓰인 카드 한 장을 뽑는 게임이다.
# 게임의 룰은 아래와 같다.
# 1. 숫자 카드가 쓰인 카드들이 N x M 형태로 놓여 있다. 이때 N은 행의 개수, M은 열의 개수이다.
# 2. 먼저 행을 선택한다.
# 3. 선택된 행에서 가장 숫자가 낮은 카드를 뽑는다.
# 첫째 줄에 숫자 카드들이 놓인 행 N과 열 M이 공백을 기준으로 각각 자연수로 주어진다. (1 <= N, M <= 100)
# 둘째 줄부터 N개의 줄에 걸쳐 각 카드에 적힌 숫자가 주어진다. 각 숫자는 1~10000의 자연수
# 첫째 줄에 게임의 룰에 맞게 선택한 카드에 적힌 숫자를 출력한다.


import sys

square = []
n, m = map(int, sys.stdin.readline().split())
for i in range(n):
    square.append(list(map(int, sys.stdin.readline().split())))

print(square)
# 풀이
# 각 행에서 가장 작은 수를 뽑는다.
# 각 행의 가장 작은 수들을 비교하여 가장 큰 수를 뽑는다.
# 가장 큰 수가 포함된 행을 구한다.
min_list = []
for row in square:
    min_list.append(min(row))
print(max(min_list))
