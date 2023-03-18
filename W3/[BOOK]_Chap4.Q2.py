n = 5

cnt = 0

for i in range(n+1):
  for j in range(60):
    for k in range(60):
      hourToStr = str(i) + str(j) + str(k)
      if hourToStr.find('3') >= 0:
        cnt += 1

print(cnt)