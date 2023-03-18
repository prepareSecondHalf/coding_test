import sys

N = int(sys.stdin.readline())

result = 0

for i in range(N):
    alphabets = list(str(sys.stdin.readline()))

    alphabetCnt = [0] * 26
    prev = -1

    for alphabet in alphabets:
        cur = ord(alphabet) - 97

        if prev != cur:
            alphabetCnt[cur] += 1
            prev = cur
    
    isSuc = True

    for cnt in alphabetCnt:
        if cnt >= 2:
            isSuc = False
    
    if isSuc:
        result += 1


print(result)