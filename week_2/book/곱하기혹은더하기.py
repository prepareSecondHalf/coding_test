import sys

# 내가 생각한 답
s = str(sys.stdin.readline())

result = int(s[0])

for i in range(1, len(s)):
	num = int(s[i])

    if result == 0 or num <= 1:
        result += num
    else:
        result *= num
        
print(result)


# 정답
s = str(input())

result = int(s[0])

for i in range(1, len(s)):
	num = int(s[i])

    if result <= 1 or num <= 1:
        result += num
    else:
        result *= num
        
print(result)