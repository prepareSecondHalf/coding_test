# 두 문자열 A, B가 주어졌을 때, A를 편집하여 B로 만든다.
# A를 편집할 때는 다음 세 연산 중 하나를 선택하여 이용할 수 있다.
# 삽입: 특정 위치의 문자열 하나 삽입
# 삭제: 특정 위치의 문자열 하나 삭제
# 교체: 특정 위치의 문자열 하나를 다른 문자열로 교체
# 편집 거리란 A를 B로 만들기 위해 사용한 연산의 수이다.
# cat => cut 편집 거리 1
# sunday => saturday 편집 거리 3
# 최소 편집 거리를 계산하는 프로그램을 작성하시오

# 두 문자열 A, B가 한 줄에 하나씩 주어진다.
# 각 문자열은 영문 알파벳으로만 구성되어 있고, 길이는 1~5000이다.

# 최소 편집 거리를 출력한다.

import sys
a = sys.stdin.readline();
b = sys.stdin.readline();

m = len(a)  # 문자열 A의 길이
n = len(b)  # 문자열 B의 길이

# 2차원 DP 테이블 초기화
dp = [[0] * (n+1) for _ in range(m+1)]

# 초기값 설정
for i in range(m+1):
    dp[i][0] = i
for j in range(n+1):
    dp[0][j] = j

# 최소 편집 거리 계산
for i in range(1, m+1):
    for j in range(1, n+1):
        # 문자가 같을 경우
        if a[i-1] == b[j-1]:
            dp[i][j] = dp[i-1][j-1]
        # 문자가 다를 경우
        else:
            dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])+1
print(dp[m][n])