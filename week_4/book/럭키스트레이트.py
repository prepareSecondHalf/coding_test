import sys

s = str(sys.stdin.readline().strip())

left = s[0:len(s) // 2]
right = s[len(s) // 2:]

leftSum = sum([int(x) for x in left])
rightSum = sum([int(x) for x in right])

if leftSum == rightSum:
    print("LUCKY")
else:
    print("READY")