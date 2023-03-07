# 길이가 N인 정수 배열 A와 B가 있다. 함수 S는 다음과 같다.
# S = A[0] X B[0] + ... + A[N-1] X B[N-1]
# S의 값을 가장 작게 만들기 위해 A의 수를 재배열하자. B는 재배열할 수 없다.
# S의 최솟값을 출력하는 프로그램을 작성하시오

# 첫째 줄에 N이 주어진다. 
# 둘째 줄에는 A에 있는 N개의 수가 순서대로 주어지고, 셋째 줄에는 B에 있는 수가 순서대로 주어진다.
# N은 50보다 작거나 같은 자연수이고, A와 B의 각 원소는 100보다 작거나 같은 음이 아닌 정수이다.

# 첫째 줄에 S의 최솟값을 출력한다.

# 풀이: A를 재배열한 결과를 구하는게 아니고... 최솟값을 구하면 됨
# 곱셈의 결과값을 줄이려면 작은수 x 큰수를 많이 만들어야 하므로 min(A) * max(B) 하면 될 듯
# 시간 복잡도는 n
import sys
n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
b = list(map(int, sys.stdin.readline().split()))

result = 0
for i in range(n):
    minA = min(a)
    maxB = max(b)
    result += minA * maxB
    a.remove(minA)
    b.remove(maxB)
print(result)