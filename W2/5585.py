import sys

pay = 1000
price = int(sys.stdin.readline())

change = pay - price
res = 0

while change>0:
  if change//500 > 0:
    res += change//500
    change = change - (500 * (change//500))
  elif change//100 > 0:
    res += change//100
    change = change - (100 * (change//100))
  elif change//50 > 0:
    res += change//50
    change = change - (50 * (change//50))
  elif change//10 > 0:
    res += change//10
    change = change - (10 * (change//10))
  elif change//5 > 0:
    res += change//5
    change = change - (5 * (change//5))
  elif change//1 > 0:
    res += change//1
    change = change - (1 * (change//1))
    
print(res)