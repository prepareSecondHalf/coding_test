# 못생긴 수는 2, 3, 5만을 소인수로 가지는 수를 의미합니다.
# 1도 못생긴 수라고 가정합니다.
# 따라서 못생긴 수는 1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15... 순으로 이어집니다.
# n번째 못생긴 수를 찾는 프로그램을 작성하세요.

# 첫째 줄에 n이 입력된다. (1 <= n <= 1000)

# n번째 못생긴 수를 출력한다.

import sys
n = int(sys.stdin.readline())

# 못생긴 수들이 들어갈 dp table
ugly_numbers = [1]
i2 = 0
i3 = 0
i5 = 0

while len(ugly_numbers) < n:
    next_ugly = min(ugly_numbers[i2]*2, ugly_numbers[i3]*3, ugly_numbers[i5]*5)
    ugly_numbers.append(next_ugly)

    # update index
    if next_ugly == ugly_numbers[i2]*2: 
        i2 += 1
    if next_ugly == ugly_numbers[i3]*3: 
        i3 += 1
    if next_ugly == ugly_numbers[i5]*5: 
        i5 += 1
print(ugly_numbers)
print(ugly_numbers[n-1])