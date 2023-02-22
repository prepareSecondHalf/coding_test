# 당신은 음식점의 계산을 도와주는 점원이다. 카운터에는 거스름돈으로 사용할 500원, 100원, 50원, 10원짜리 동전이 무한히 존재한다.
# 손님에게 거슬러 줘야 할 돈이 N원일 때 거슬러 줘야 할 동전의 최소 개수를 구하라. 단, 거슬러 줘야 할 돈 N은 항상 10의 배수이다.

# first try
n = int(input())
coins = [500, 100, 50, 10]
number_of_coins = 0

for coin in coins:
    number_of_coins += n // coin
    n = n % coin
print(number_of_coins, '개')