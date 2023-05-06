import sys

N = int(sys.stdin.readline())

cards = []

for _ in range(N):
	cards.append(int(sys.stdin.readline()))

cards.sort()

result = 0
prev = 0

if N >= 2:
	for i in range(1, N):
		prev += cards[i - 1]
		result += prev + cards[i]

print(result)

# 풀이는 위 방식처럼 정렬해서 앞에서부터 더하는게 맞는데.... 우선순위 큐를 써야된다고 한다.
# 보통 Queue라고 하면 그냥 선형적인 FIFO 형태이지만 우선순위 큐는 트리 형태를 띄며 보통 Heap과 연결지어 설명된다.
# Max Heap, Min Heap을 코테 준비 과정에서는 우선순위 큐라고 쓰는듯? 
# 우선순위 큐 자체가 저것들을 의미하는 것은 아니나 보통 우선순위를 둘 때 조건을 Max, Min을 두고 나오니 저 2개가 대표적인 것 같다.
import sys
import heapq

input = sys.stdin.readline

n = int(input())
cards = []
for i in range(n):
    heapq.heappush(cards, int(input()))

result = 0

if len(cards)==1:
    print(result)

else:
    for i in range(n-1): # 2개씩 꺼내기 떄문에 n-1
        previous = heapq.heappop(cards)
        current = heapq.heappop(cards)

        result += previous + current
        heapq.heappush(cards,previous + current)
    
    print(result)