import sys

# 내 정답
N = int(str, sys.stdin.readline())

cnt = 0

for i in range((N + 1) * 60 * 60):
    s = str(i % 60)
    m = str(i % 3600 // 60)
    h = str(i // 3600)
    
    if '3' in h + m + s:
        cnt += 1
        
print(cnt)