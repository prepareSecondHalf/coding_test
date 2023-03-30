from collections import deque

# 큐 구현을 위해 deque 라이브러 시용
queue = deque()

queue.append(5)
queue.append(2)
queue.append(7)
# 맨 앞 데이터 꺼냄
queue.popleft()
queue.append(1)
queue.append(4)
queue.popleft()

print(queue)
print(list(queue))

