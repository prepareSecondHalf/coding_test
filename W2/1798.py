import sys

a = int(sys.stdin.readline())

sum = 0
cnt = 0

while(True):
    cnt += 1
    sum += cnt
    if sum>a: 
        sum -= cnt
        cnt -= 1
        break
    
print(cnt)