# 요세푸스 문제는 다음과 같다.
# 1번부터 N번까지 N명의 사람이 원을 이루면서 앉아있고, 양의 정수 K(≤ N)가 주어진다. 
# 이제 순서대로 K번째 사람을 제거한다. 
# 한 사람이 제거되면 남은 사람들로 이루어진 원을 따라 이 과정을 계속해 나간다. 
# 이 과정은 N명의 사람이 모두 제거될 때까지 계속된다. 
# 원에서 사람들이 제거되는 순서를 (N, K)-요세푸스 순열이라고 한다. 
# 예를 들어 (7, 3)-요세푸스 순열은 <3, 6, 2, 7, 5, 1, 4>이다.
# N과 K가 주어지면 (N, K)-요세푸스 순열을 구하는 프로그램을 작성하시오.

# 첫째 줄에 N과 K가 빈 칸을 사이에 두고 순서대로 주어진다. (1 ≤ K ≤ N ≤ 1,000)

# 예제와 같이 요세푸스 순열을 출력한다.
from collections import deque
import sys
n, k = map(int, sys.stdin.readline().split())

# 문제 예시를 보아하니 제거된 사람이 첫 번째 순서가 되는 듯?
# 이 친구도 deque를 이용하면 좋을 것 같다... 
result = []
people = deque(list(range(1, n+1)))
curr_idx = 0
while len(people) != 0:
    if curr_idx == k - 1:
        result.append(people.popleft())
        curr_idx = 0
    else:
        people.append(people.popleft())
        curr_idx += 1
resultStr = '<'+ ", ".join(str(num) for num in result) +'>'
print(resultStr)