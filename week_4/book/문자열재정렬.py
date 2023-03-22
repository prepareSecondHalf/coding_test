import sys

data = list(sys.stdin.readline().strip())

strs = [x for x in data if x.isalpha()]
nums = [int(x) for x in data if not x.isalpha()]

strs.sort()

print(''.join(strs) + str(sum(nums)))