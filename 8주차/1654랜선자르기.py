# k: 가지고 있는 랜선의 개수, n: 필요한 랜선의 개수
# 2번째줄 ~ k+1번째 줄: 랜선의 길이(cm)
# 출력: n개를 만들 수 있는 랜선의 최대 길이
import sys

k, n = map(int, sys.stdin.readline().split())
lan = [int(sys.stdin.readline()) for _ in range(k)]
start, end = 1, max(lan)  # 이분탐색 처음과 끝위치

while start <= end:
    mid = (start + end) // 2  # 중간값
    lines = 0  # 랜선 수
    for i in lan:
        lines += i // mid  # 각 랜선길이를 중간값으로 나눈 몪을 line에 계속 더해줌(랜선의 수)

    if lines >= n:  # 필요한 랜선의 수보다 크거나 같을경우 start값을 늘림
        start = mid + 1
    else: # 필요한랜선의 수보다 적을 경우 end값을 줄임
        end = mid - 1
print(end)
