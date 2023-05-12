# n: 수열안의 원소의 개수, x: 수열안에 몇개 있는지 확인해야할 수
# 출력: 수열안에 x의 개수
import sys

n, x = map(int, sys.stdin.readline().split())
array = list(map(int, sys.stdin.readline().split()))
start = 0
end = n-1
cnt = 0

while start <= end:
    mid = (start + end) // 2
    # 중간값이 x일때 좌우 확인 및 cnt+1후 좌우 다 확인되면 break
    if x == array[mid]:
        for i in range(mid, -1, -1):
            if array[i] == x:
                cnt += 1
            else:
                break
        for j in range(mid + 1, len(array)):
            if array[j] == x:
                cnt += 1
            else:
                break
        break
    elif x > array[mid]:
        start = mid + 1
    else:
        end = mid - 1

if cnt == 0:
    print(-1)
else:
    print(cnt)
 