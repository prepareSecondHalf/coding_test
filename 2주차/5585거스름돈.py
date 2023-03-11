import sys

money = int(sys.stdin.readline())
last_money = int(1000 - money)
a = int(last_money / 500)
b = int((last_money - (a*500)) /100)
c = int((last_money - (a*500) - (b*100))/50)
d = int((last_money - (a*500) - (b*100) - (c*50)) / 10)
e = int((last_money - (a*500) - (b*100) - (c*50)- (d*10)) / 5)
f = int((last_money - (a*500) - (b*100) - (c*50) - (d*10)- (e*5)) / 1)
print(a+b+c+d+e+f)
