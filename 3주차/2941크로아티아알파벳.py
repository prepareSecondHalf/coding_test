import sys

word = sys.stdin.readline()
croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
count = 0
for i in range(len(croatia)):
    word = word.replace(croatia[i], '*')
print(len(word)-1)
