# n: 집의 수
# 색칠 비용(빨강, 초록, 파랑)
# 출력: 모든집을 칠하는 비용의 최솟값
# 조건
# 1. 1번 집의 색은 2번 집의 색과 같지 않아야 한다
# 2. N번 집의 색은 N-1번 집의 색과 같지 않아야 한다
# 3. i(2 ≤ i ≤ N-1)번 집의 색은 i-1번, i+1번 집의 색과 같지 않아야 한다.
import sys

n = int(sys.stdin.readline())
rgb = []
for _ in range(n):
    rgb.append(list(map(int, sys.stdin.readline().split())))

for i in range(1, len(rgb)):
    #빨간색
    rgb[i][0] = min(rgb[i - 1][1], rgb[i - 1][2]) + rgb[i][0] #이전집은 빨간색을 제외한값중에 작은값 + 현위치빨간색값을 현위치 빨간색값에 삽입
    #초록색
    rgb[i][1] = min(rgb[i - 1][0], rgb[i - 1][2]) + rgb[i][1] #이전집은 초로색을 제외한값중에 작은값 + 현위치초록색값 현위치 초록색값에 삽입
    #파란색
    rgb[i][2] = min(rgb[i - 1][0], rgb[i - 1][1]) + rgb[i][2] #이전집은 파란색을 제외한값중에 작은값 + 현위치파란색값 현위치 파란색값에 삽입

# 위에 구한 빨간색, 초록색, 파란색값중에 최소값을 출력
print(min(rgb[n - 1][0], rgb[n - 1][1], rgb[n - 1][2]))