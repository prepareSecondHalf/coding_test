import sys

arr = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
word = sys.stdin.readline().strip()

for i in arr:
    word = word.replace(i, '?')

print(len(word))