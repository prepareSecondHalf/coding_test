# 알파벳 대문자와 숫자 0~9로만 구성된 문자열이 입력으로 주어진다. 
# 이 때 모든 알파벳을 오름차순으로 정렬하여 이어서 출력한 뒤, 모든 숫자를 더한 값을 이어서 출력하라

# 첫째 줄에 문자열 S가 주어진다. (1 <= S의 길이 <= 10,000)

# 첫째 줄에 답을 출력한다.

import sys
s = sys.stdin.readline().strip()
# 풀이: 반복문 돌려서 문자열 배열, 숫자 배열로 나눈 뒤 더한다.
strs = []
nums = []
for char in s:
    if str.isdigit(char):
        nums.append(int(char))
    else:
        strs.append(char)
result = ''.join(sorted(strs)) + str(sum(nums))
print(result)