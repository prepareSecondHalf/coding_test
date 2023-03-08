# 처음 푼 코드
# 뭔진 모르겠지만 Runtime Error
import sys

s = list(map(str, sys.stdin.readline().strip().split('-')))

result = eval(s[0])

if len(s) > 1:
    for i in range(1, len(s)):
        result -= eval(s[i])

print(result)

# 예전에 풀었던 코드
import sys

s = list(map(str, sys.stdin.readline().strip().split('-')))

number = []

for data in s:
    number.append(sum(map(int, data.split('+'))))

print(number[0] - sum(number[1:]))