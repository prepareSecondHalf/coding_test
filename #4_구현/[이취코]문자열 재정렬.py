'''
    알파벳 대문자 + 숫자(0~9) 조합 무낮열
    알파벳 오름차순 > 출력
    나머지 숫자의 합 > 출력
    K1KA5CB7
'''

import sys

input = sys.stdin.readline()
strs = ''
nums = ''

for i in input:
  if i.isalpha() == True: strs += i
  else: nums += i

strs = list(strs)
nums = list(nums.replace('\n', ''))
# nums = list(map(int, nums))

strs = sorted(strs)
nums = sorted(nums)
nums = map(int, nums)

print(''.join(strs), end='')
print(sum(nums))