# n: 삼각형의 크기
# 2 ~ n+1줄까지 정수삼각형 입력
# 조건: 맨위부터 왼쪽아래대각선, 오른쪽아래 대각선으로만 이동가능
# 출력: 선택된수의 합의 최대값
#     7
#    3 8
#   8 1 0
#  2 7 4 4
# 4 5 2 6 5
# triangle[i+1][j] or triangle[i+1][j+1]
import sys

n = int(sys.stdin.readline())
triangle = []
for _ in range(n):
    triangle.append(list(map(int, sys.stdin.readline().split())))
for i in range(1, n):
    for j in range(len(triangle[i])):

        # 가장자리 정수 제외 왼쪽위에꺼랑 오른쪽위에꺼중 큰걸 더해서 넣어준다
        if len(triangle[i])-1 != j and j != 0:
            triangle[i][j] = max(triangle[i-1][j-1]+triangle[i][j], triangle[i-1][j]+triangle[i][j])

        # 정수가 왼쪽변에 있을때 오른쪽위에 정수를 더해서 넣어준다
        elif j == 0:
            triangle[i][j] = triangle[i-1][j] + triangle[i][j]

        # 정수가 오른쪽변에 있을때 왼쪽위에 정수를 더해서 넣어준다
        else:
            triangle[i][j] = triangle[i - 1][j-1] + triangle[i][j]

# triangle 마지막요소중에 가장 큰수를 출력
print(max(triangle[n-1]))