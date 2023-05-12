# n: 원소의 개수
# n개의 원소를 공백으로 구분
import sys

n = int(sys.stdin.readline())
array = list(map(int, sys.stdin.readline().split()))

start = 0
end = n-1

while start <= end:
    mid = (start + end) // 2
    if array[mid] == mid:
        print(mid)
        break
    # 원소가 인덱스보다 작으면 좌측값은 고정점이 될수없음
    elif array[mid] < mid:
        start = mid + 1
    else:
        end = mid - 1

if array[mid] != mid:
    print(-1)