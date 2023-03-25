# 내 코드
# 이것도 참 답이 없다...
# 각 취약점 사이의 거리를 구해 큐에 저장하고 내림차순 정렬
# 취약점 사이 거리가 가장 긴 것을 하나씩 제거하면서 반복문 진행. 이때, 취약점 사이 거리가 가장 긴 것을 하나씩 제거할 때마다 사람 수는 늘어난다.
# 진행하다가 취약점 사이의 거리를 담은 배열에 남은게 없어졌으면 안되는 것이므로 -1 리턴
# 이라고 풀었는데... 이렇게 해서 될 리가 없지 ㅎㅎ
from collections import deque

def solution(n, weak, dist):
    answer = 0
    weak_dist = [] # 각 취약점 사이 거리
    
    dist.sort(reverse=True)
        
    for i in range(len(weak) - 1):
        weak_dist.append(weak[i + 1] - weak[i])
    
    # 맨 마지막 취약점과 맨 처음 취약점 사이 거리
    weak_dist.append((n - weak[-1]) + weak[0])
    
    # 거리 내림차순
    weak_dist.sort(reverse=True)
    weak_dist = deque(weak_dist)
    
    i = 1
    
    while True:
        wd_len = len(weak_dist)
        
        # 거리가 하나도 남지 않았으면
        if wd_len <= 0:
            answer = -1
            break
        
        # 최대값은 빼주기
        weak_dist.popleft()
        
        # 최대 친구들 i번째까지 가져오기
        tmp_dist = [dist[i] for i in range(0, i)]
        
        # 남은 거리 <= 친구들이 할 수 있는 값의 합
        if sum(weak_dist) <= sum(tmp_dist):
            answer = i
            break
        else:
            i += 1
    
    return answer
    
# 정답 코드
from itertools import permutations # 순열

def solution(n, weak, dist):
    # 길이를 2배로 늘려 원형을 일자 형태로 변경
    # 자물쇠와 열쇠 문제도 그렇고 이렇게 좀 구조를 바꾸는 형태가 종종 있나보다
    length = len(weak)
    for i in range(length):
        weak.append(weak[i] + n)
    answer = len(dist) + 1 # 투입할 친구 수의 최소값을 찾아야 하므로 나올 수 없는 값으로 초기화
    
    # 0부터 length - 1까지의 위치를 각각 시작점으로 설정
    for start in range(length):
        # 친구를 나열하는 모든 경우의 수 각각에 대해 확인
        for friends in list(permutations(dist, len(dist))):
            count = 1 # 투입할 친구 수
            position = weak[start] + friends[count - 1] # 해당 친구가 점검할 수 있는 마지막 위치
            
            for index in range(start, start + length): # 시작점부터 모든 취약 지점 확인
                if position < weak[index]: # 점검할 수 있는 위치를 벗어나는 경우
                    count += 1 # 새 친구 투입
                    if count > len(dist): # 더 투입 불가능하면 종료
                        break
                    
                    position = weak[index] + friends[count - 1]
                    
            answer = min(answer, count)
            
    if answer > len(dist):
        return -1
        
    return answer