# n: 배달해야할 설탕무게
# 출력: 3kg, 5kg의 봉지로 나눠 배달할때 최소한의 봉지 개수 (정확하게 나눠담을수 없을때 -1을 출력)

# 접근방식: 5kg으로 나누어떨어지면 몫을 cnt에 더하고 break 아닐경우 3을빼가면서 cnt에 1을 더해주면서 n이 0 이하가 될때까지 while문을 돌림
import sys

n = int(sys.stdin.readline())
cnt = 0

while n >= 0:
    if n % 5 == 0:
        cnt += (n // 5)
        break
    n -= 3
    cnt += 1

if n < 0:
    cnt = -1
print(cnt)


