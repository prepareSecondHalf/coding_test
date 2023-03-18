import sys

n = int(sys.stdin.readline())
cnt = 0


for i in range(n):
  dup = True
  word = sys.stdin.readline()
    
  for j in range(len(word)-1):    
    if word[j] == word[j+1]:
      next
    elif word[j] in word[j+1:]:
      dup = False
      break

  if dup:
    cnt += 1

print(cnt)