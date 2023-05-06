def solution(N, stages):
    answer = []
    
    arr = []
    
    for i in range(1, N + 1):
        tmpLen = len([x for x in stages if x >= i])
        target = stages.count(i)
        
        arr.append((i, target / tmpLen))
        
    arr = sorted(arr, key=lambda x: -x[1])

    for info in arr:
        answer.append(info[0])
        
    return answer

print(solution(4, [4, 4, 4, 4, 4]))

# 정답
# 위 코드에서 7번째 줄이 속도에 영향을 많이 줄거같긴 했는데... 확실히 ㅎ...
def solution(N, stages):
    answer = []
    length = len(stages)

    for i in range(1, N + 1):
        target = stages.count(i)
        
        if(length == 0):
            fail = 0
        else:
            fail = target / length

        answer.append((i, fail))
        length -= target
        
    answer = sorted(answer, key=lambda x: x[1], reverse=True)

    answer = [i[0] for i in answer]
        
    return answer

print(solution(4, [4, 4, 4, 4, 4]))