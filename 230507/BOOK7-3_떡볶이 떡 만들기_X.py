# 여행 가신 부모님을 대신해 떡볶이 떡을 만든다.
# 떡의 길이가 일정하지 않다. 한 봉지 안에 들어가는 떡의 총 길이는 절단기로 잘라 맞춘다.
# 절단기에 높이 H를 지정하면 줄지어진 떡을 한 번에 절단한다.
# H보다 긴 떡은 긴 만큼 잘리고, 짧은 떡은 잘리지 않는다.
# 손님은 잘린 만큼의 떡을 가져간다.
# 손님이 요청한 총 길이가 M일 때, 적어도 M만큼의 떡을 얻기 위해 설정할 수 있는 높이의 최댓값은?

# 입력
# 첫째 줄에 떡의 개수 N과 요청한 떡의 길이 M이 주어진다. (1 <= N <= 1000000) (1 <= M <= 2000000000)
# 둘째 줄에 떡의 개별 높이가 주어진다. 떡 높이의 총합은 항상 M 이상이다.

# 출력
# 적어도 M만큼의 떡을 가져가기 위해 절단기에 설정할 수 있는 높이의 최댓값을 출력

import sys
n, m = map(int, sys.stdin.readline().split())
heights = list(map(int, sys.stdin.readline().split()))

# 풀이
# 제일 긴 떡 기준으로 이진 탐색하되
# 각 탐색마다 잘린 떡의 길이의 합을 구해 비교

def binary_search(data, target):
    data.sort()
    start = 0
    end = len(data) - 1

    while start <= end:
        center = (start + end) // 2
        candidate = data[center] # 절단기 높이 후보
        sum = 0 # 잘린 떡의 길이의 합
        for height in heights: # 모든 떡 중, 절단기보다 높은 친구들은 잘린 부분 더함
            if height > candidate:
                sum += height - candidate
                
        if sum == target: # 잘린 떡의 길이의 합이 target과 일치하면 절단기 높이 반환
            return candidate
        elif sum > target: # 크면 start 변경
            start = center + 1
        elif sum < target: # 작으면 end 변경
            end = center - 1

max_height = max(heights)
candidates = list(range(max_height)) # 제일 긴 떡에 대해 이진 탐색
answer = binary_search(candidates, m)

print(answer)