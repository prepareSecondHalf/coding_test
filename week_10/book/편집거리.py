# 아이디어도 안떠오름
# 해설 보니까 걍 공식이 있는 문제네
# 다 이런 문제만 있는거 보니까 여기 나온 예시들 주구장창 외워서 문제 푸는게 맞을듯

def edit_dist(str1, str2):
    n = len(str1)
    m = len(str2)

    dp = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        dp[i][0] = i
    for j in range(i, m + 1):
        dp[0][j] = j

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i][j - 1], dp[i - 1][j], dp[i - 1][j - 1])
    
    return dp[n][m]

str1 = input()
str2 = input()

print(edit_dist(str1, str2))