# 백준 42889
# n: 전체 스테이지의 개수, stage: 사용자가 현재 멈춰있는 스테이지의 번호가 담긴 배열
# 실패율이 높은스테이지부터 내림차순으로 스테이지의 번호가 담겨있는 배열을 리턴

def solution(N, stages):
    answer = []
    ratio = {}
    # 전체 플레이어 수 > 스테이지 지날수록 줄어든다
    player = len(stages)

    for i in range(1, N + 1):
        if player == 0:  # 멈춰있는 스테이지가 없을때 ratio에 0을 추가
            ratio[i] = 0
        else:
            ratio[i] = stages.count(i) / player
            player -= stages.count(i)  # 현재 스테이지에 멈춘 숫자만큼 제외

    # value 기준으로 정렬 후 key 저장
    answer = sorted(ratio, key=lambda x: ratio[x], reverse=True)

    return answer