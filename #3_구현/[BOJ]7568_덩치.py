'''
  첫 요소의 키와 몸무게를 맥스라고 둔다
  그냥 자기보다 크고 무거운(둘 다 큰) 사람이 몇 명인지 쟤서 자기 등수만 정하면 된다. 
  n명을 n-1번씩 전수 비교해보면 된다.
'''

people = int(input())
li = []

for _ in range(people):
  weight, height = map(int, input().split())
  li.append((weight, height))



for y in li:
  rank = 1

  for x in li:
    if (y[0] < x[0] and y[1] < x[1]):
      rank += 1
  print(rank, end = " ")