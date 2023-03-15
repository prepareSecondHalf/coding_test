# 왕실의 정원이 체스판과 같은 8 x 8 좌표 평면이다.
# 특정 한 칸에 나이트가 서 있다.
# 이동을 할 때는 L자 형태로만 이동이 가능하며, 정원 밖으로 나갈 수 없다.
# 수평으로 두 칸 이동한 뒤 수직으로 한 칸 이동하거나
# 수직으로 두 칸 이동한 뒤 수평으로 한 칸 이동할 수밖에 없다.
# 이동할 수 있는 경우의 수를 출력하는 프로그램을 작성하시오.
# 행은 1~8로 표현하고 열은 a~h로 표현한다.

# 첫째 줄에 8 x 8에서 현재 위치한 곳의 좌표를 열과 행의 두 문자로 입력된다. (a1, b2 등)

# 첫째 줄에 경우의 수를 출력한다.

import sys
curr_coord_str = sys.stdin.readline().strip()
# 풀이
# 열(x)은 a~h이지만 1~8로 바꿔서(ord - 96) 계산하면 편할 것... 경우의 수를 체크하면 되므로 다시 바꿀 필요도 없다.
curr_coord = [ord(curr_coord_str[0]) - 96, int(curr_coord_str[1])]
print(curr_coord)
# 이후로는 경우의 수(최대 8가지, 방향 동서남북4 x 수평or수직2) => [+-2, +-1], [+-1, +-2]
# 를 계산해서 1보다 작거나 8보다 큰 경우 무시하고 카운팅
cases = [[2, 1], [-2, 1], [2, -1], [-2, -1], [1, 2], [-1, 2], [1, -2], [-1, -2]]
number_of_cases = 0
for case in cases:
    if curr_coord[0] + case[0] < 1 or curr_coord[0] + case[0] > 8 or curr_coord[1] + case[1] < 1 or curr_coord[1] + case[1] > 8:
        continue
    else:
        number_of_cases += 1
print(number_of_cases)
