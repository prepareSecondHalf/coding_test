# n: 식량창고의 개수
# 각 식량창고에 저장된 식량의 개수
# 출력: 개미전사가 얻을수 있는 식량의 최댓값
# 개미는 한칸이상 떨어진 식량창고를 약탈해야할때 약탈할수 있는 식량의 최댓값
import sys

n = int(sys.stdin.readline())
food = list(map(int, sys.stdin.readline().split()))
d = [0] * 100 # n은 최대 100까지 들어올수있음

d[0] = food[0]
d[1] = max(food[0], food[1])

for i in range(2, n):
    # i-1번째 최적의해와 i-2에 현재값을 더한것중 더 큰걸 삽입
    d[i] = max(d[i - 1], d[i - 2] + food[i])

print(d[n-1])

