# n: 떡의 개수, m: 요청한 떡의 길이
# 떡의 개별 높이
# 출력: m 만큼의 떡을 가져가기위해 절단기에 설정할수있는 높이의 최댁값
import sys

n, m = map(int, sys.stdin.readline().split())
thug = list(map(int, sys.stdin.readline().split()))
start = 0
end = max(thug)
result = 0
while start <= end:
    total = 0
    mid = (start + end) // 2
    # 떡을 중간값으로 잘라서 잘린부분을 total에 더해줌
    for x in thug:
        if x > mid:
            total += x - mid

    #total이 필요한떡의 길이(m)보다 작으면 end값을 내리고 다시 while문
    if total < m:
        end = mid - 1
    # total이 m보다 크거나 같을경우 result에 mid값을 넣어주고 start값을 올려서 다시 while문
    else:
        result = mid
        start = mid + 1
# start값이 end값보다 커지면 while문 종료후 result 출력
print(result)