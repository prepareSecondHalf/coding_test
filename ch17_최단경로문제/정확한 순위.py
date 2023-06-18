'''
    학생들 성적 비교 결과 주어질 때, 성적 순위 알 수 있는 학생 모두 몇 명인지
'''

n, m = list(map(int, input().split()))
# 학생들의 성적 비교가 가능한 경우의 인접행렬
array = [[1e9] * (n + 1) for i in range(n + 1)]

# 초기 비교 횟수 입력
for i in range(m):
    A, B = list(map(int, input().split()))
    array[A][B] = 1

# 자기 자신과 비교하는 경우는 0으로 입력
for i in range(n + 1):
    array[i][i] = 0

# i -> k -> j가 i -> j보다 작다면 값을 교체
for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            array[i][j] = min(array[i][k] + array[k][j], array[i][j])

result = 0

# A -> B인 경우와 B -> A인 경우 중 최단 거리를 구했다면, count를 증가시킴.
# count가 학생수와 같다면 결과값을 증가시킴.
for i in range(1, n + 1):
    count = 0
    for j in range(1, n + 1):
        if array[i][j] != 1e9 or array[j][i] != 1e9:
            count += 1
    
    if count == n:
        result += 1

print(result)
