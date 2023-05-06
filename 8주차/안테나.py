# 백준 18310
# n: 집의 수
# n채의 집의 위치
# 출력: 안테나를 설치할 위치의 값(여러개일경우 가장 작은값)
import sys

n = int(sys.stdin.readline())
home = sorted(list(map(int, sys.stdin.readline().split())))
print(home[(n-1)//2])
# home을 오름차순으로 정렬후 가운데값 출력