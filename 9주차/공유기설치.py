# 백준 2110
# n: 집의개수, c: 공유기의 개수
# 집의좌표를 나타내는 x가 한줄에 하나씩 주어진다
# 출력: 가장 인접한 공유기사이의 최대 거리
import sys

n, c = map(int, sys.stdin.readline().split())
home = sorted([int(sys.stdin.readline()) for _ in range(n)])

def solution(home, start, end):
    while start <= end:
        mid = (start + end) // 2
        current = home[0]
        count = 1

        for i in range(1, len(home)):
            if home[i] >= current + mid:
                count += 1
                current = home[i]

        if count >= c:
            global answer
            start = mid + 1
            answer = mid
        else:
            end = mid - 1


start = 1
end = home[-1] - home[0]
answer = 0

solution(home, start, end)
print(answer)
