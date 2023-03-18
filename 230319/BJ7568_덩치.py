# N명의 집단에서 각 사람의 덩치 등수는 자신보다 더 "큰 덩치"의 사람의 수로 정해진다. 만일 자신보다 더 큰 덩치의 사람이 k명이라면 그 사람의 덩치 등수는 k+1이 된다. 이렇게 등수를 결정하면 같은 덩치 등수를 가진 사람은 여러 명도 가능하다. 아래는 5명으로 이루어진 집단에서 각 사람의 덩치와 그 등수가 표시된 표이다.
# 이름	(몸무게, 키)	덩치 등수
# A 	(55, 185)   	2
# B 	(58, 183)   	2
# C 	(88, 186)   	1
# D 	(60, 175)   	2
# E 	(46, 155)   	5
# 위 표에서 C보다 더 큰 덩치의 사람이 없으므로 C는 1등이 된다. 그리고 A, B, D 각각의 덩치보다 큰 사람은 C뿐이므로 이들은 모두 2등이 된다. 그리고 E보다 큰 덩치는 A, B, C, D 이렇게 4명이므로 E의 덩치는 5등이 된다. 위 경우에 3등과 4등은 존재하지 않는다. 여러분은 학생 N명의 몸무게와 키가 담긴 입력을 읽어서 각 사람의 덩치 등수를 계산하여 출력해야 한다.

# 첫 줄에는 전체 사람의 수 N이 주어진다. 그리고 이어지는 N개의 줄에는 각 사람의 몸무게와 키를 나타내는 양의 정수 x와 y가 하나의 공백을 두고 각각 나타난다.

# 여러분은 입력에 나열된 사람의 덩치 등수를 구해서 그 순서대로 첫 줄에 출력해야 한다. 단, 각 덩치 등수는 공백문자로 분리되어야 한다.

# 2 ≤ N ≤ 50
# 10 ≤ x, y ≤ 200

import sys
n = int(sys.stdin.readline().strip())

people = []
for person in range(n):
    x, y = list(map(int, sys.stdin.readline().split()))
    people.append([x, y])

# n, x, y가 작으므로 n^2 가능
rank_data = []
for target in range(n):
    rank = 1
    for comparison in range(n):
        if people[target][0] < people[comparison][0] and people[target][1] < people[comparison][1]:
            rank += 1
    rank_data.append(rank)
print(*rank_data, sep=" ")