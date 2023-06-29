import sys
s = sys.stdin.readline()
sum = 0
num = 1
numArr = []

while sum < int(s):
    numArr.append(num)
    sum += num
    num += 1

print(len(numArr)) if int(s) == sum else print(len(numArr) - 1) 