# 그룹 단어란 단어에 존재하는 모든 문자에 대해서, 각 문자가 연속해서 나타나는 경우만을 말한다. 예를 들면, ccazzzzbb는 c, a, z, b가 모두 연속해서 나타나고, kin도 k, i, n이 연속해서 나타나기 때문에 그룹 단어이지만, aabbbccb는 b가 떨어져서 나타나기 때문에 그룹 단어가 아니다.
# 단어 N개를 입력으로 받아 그룹 단어의 개수를 출력하는 프로그램을 작성하시오.

# 첫째 줄에 단어의 개수 N이 들어온다. N은 100보다 작거나 같은 자연수이다. 둘째 줄부터 N개의 줄에 단어가 들어온다. 단어는 알파벳 소문자로만 되어있고 중복되지 않으며, 길이는 최대 100이다.

# 첫째 줄에 그룹 단어의 개수를 출력한다.

import sys
n = int(sys.stdin.readline().strip())

words = []
for i in range(n):
    words.append(sys.stdin.readline().strip())

# 각 문자에 대해, 
# 1. 문자가 이전 문자와 같은지 체크
# 2. 같으면 continue(연속됨)
# 3. 이전 문자와 다르면 used 배열에 있는지 체크
# 4. 있으면 그룹 단어 아니므로 그냥 break
# 5. 없으면 그룹 단어일 가능성이 남아 있으므로 used에 넣고 계속 반복
number_of_group_word = 0
for word in words:
    used = []
    prevChar = ''
    is_group = True
    for char in word:
        if char == prevChar:
            continue
        else:
            prevChar = char
            if char in used:
                is_group = False
                break
            else:
                used.append(char)
    if is_group:
        number_of_group_word += 1

print(number_of_group_word)