# 내가 짠 코드 : 통과 안 됨
# 실패율 = (스테이지 도달 && 클리어 못한 플레이어 수) / 스테이지 도달 플레이어 수
# 실패율이 높은 스테이지부터 내림차순
def solution(N, stages):
    result = []
    n = len(stages)
    for idx in range(1, N + 1):
        counting = stages.count(idx)
        try:
            result.append([idx, counting / n])
            n = n - counting
        except ZeroDivisionError:
            continue
    
    # 각 스테이지의 번호를 실패율의 내림차순으로 정렬하면 다음과 같다.
    result = sorted(result, key=lambda x : -x[1])
    finalResult = []
    for x in result:
        finalResult.append(x[0])
    return finalResult
    

# 최종 코드
# 실패율 = (스테이지 도달 && 클리어 못한 플레이어 수) / 스테이지 도달 플레이어 수
# 실패율이 높은 스테이지부터 내림차순
def solution(N, stages):
    result = {} # 리스트 대신 딕셔너리로 교체
    n = len(stages)
    for idx in range(1, N + 1):
        counting = stages.count(idx)
        try:
            result[idx] = (counting / n)
            n = n - counting
        except ZeroDivisionError:
            result[idx] = 0
            continue
    
    # 각 스테이지의 번호를 실패율의 내림차순으로 정렬하면 다음과 같다.
    return sorted(result, key=lambda x : result[x], reverse=True)
    

        