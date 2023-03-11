# 한 마을에 모험가 N명
# 길드에서는 N명을 대상으로 공포도를 측정
# 높은 모험가는 공포를 쉽게 느껴 위기 대처 능력 낮음
# 동빈이는 안전을 위해 공포도가 X인 모험자는 X명 이상으로 구성한 그룹에 참여하도록 규정
# 만들 수 있는 최대 모험가 그룹의 수는? 반드시 모두 넣을 필요는 없다.

# 첫째 줄에 모험가의 수 N이 주어진다.
# 둘째 줄에 각 모험가의 공포도 값(N 이하의 자연수)이 공백으로 구분되어 주어진다.

# 최대 그룹 수 출력

import sys
n = int(sys.stdin.readline().strip())
fear_levels = list(map(int, sys.stdin.readline().strip().split()))

print(fear_levels)
# 풀이: 공포도가 낮은 애들을 먼저 묶어서 보낸다. 높은 애들은 못가든지 말든지 알게 뭐람
# 즉, 정렬해서 낮은 애들끼리 먼저 보내면 된다.
# 낮은 애들끼리 먼저 보내려면 첫 번째 친구의 공포도(=인원수)를 확인하고 얘네들이 그룹핑된 배열을 만든다.
# 해당 배열의 마지막 친구를 체크해 배열의 길이와 같다면 +1, 아니면 반복한다.

fear_levels.sort()
number_of_group = 0
while True:
    number_of_need = fear_levels[0]
    candidate = fear_levels[0:number_of_need]
    fear_levels = fear_levels[number_of_need:]
    if len(fear_levels) == 0:
        break
    if candidate[-1] == len(candidate):
        number_of_group += 1
    while candidate[-1] != len(candidate):
        candidate.append(fear_levels[0])
        fear_levels = fear_levels[1:]
        if fear_levels[0] > len(fear_levels):
            break
        else:
            number_of_group += 1
print('result: ', number_of_group)

# 되냐?