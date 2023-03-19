# 수를 처리하는 것은 통계학에서 상당히 중요한 일이다. 통계학에서 N개의 수를 대표하는 기본 통계값에는 다음과 같은 것들이 있다. 단, N은 홀수라고 가정하자.
# 1. 산술평균 : N개의 수들의 합을 N으로 나눈 값
# 2. 중앙값 : N개의 수들을 증가하는 순서로 나열했을 경우 그 중앙에 위치하는 값
# 3. 최빈값 : N개의 수들 중 가장 많이 나타나는 값
# 4. 범위 : N개의 수들 중 최댓값과 최솟값의 차이
# N개의 수가 주어졌을 때, 네 가지 기본 통계값을 구하는 프로그램을 작성하시오.

# 첫째 줄에 수의 개수 N(1 ≤ N ≤ 500,000)이 주어진다. 단, N은 홀수이다. 그 다음 N개의 줄에는 정수들이 주어진다. 입력되는 정수의 절댓값은 4,000을 넘지 않는다.

# 첫째 줄에는 산술평균을 출력한다. 소수점 이하 첫째 자리에서 반올림한 값을 출력한다.
# 둘째 줄에는 중앙값을 출력한다.
# 셋째 줄에는 최빈값을 출력한다. 여러 개 있을 때에는 최빈값 중 두 번째로 작은 값을 출력한다.
# 넷째 줄에는 범위를 출력한다.

import sys
n = int(sys.stdin.readline().strip())
integers = []
for i in range(n):
    integers.append(int(sys.stdin.readline().strip()))

# 시키는대로 하면 됨
# 1. 산술평균
print('the answer')
avg = sum(integers) / n
print(round(avg + 0.00001))
# 2. 중앙값 => 어차피 중앙이므로 내림차순/오름차순은 의미 x
center = sorted(integers)[len(integers) // 2]
print(center)
# 3. 최빈값 => set으로 중복 제거 => 중복 제거된 애들로 각각 count => 를 하려고 했는데 이 경우 최빈값이 중복인 경우 대응하지 못한다.
# 는 그냥 배열에 넣고 길이가 2 이상이면 정렬 후 두 번째로 작은 값
# 시간초과 > 다들 for문 두 번씩 잘만 쓰는데 왜 난 시간 초과되지???
# for문이 문제가 아니고 counter 라이브러리를 쓰지 않으면 안된다고 한다!
not_duplicated_integers = list(set(integers))
most_frequent_number = 0
most_frequently_counted = 0
most_frequent_numbers = []
for integer in not_duplicated_integers:
    if most_frequently_counted < integers.count(integer):
        most_frequently_counted = integers.count(integer)
for integer in not_duplicated_integers:
    if most_frequently_counted == integers.count(integer):
        most_frequent_numbers.append(integer)
if len(most_frequent_numbers) == 1:
    most_frequent_number = most_frequent_numbers[0]
else:
    most_frequent_number = sorted(most_frequent_numbers)[1]
print(most_frequent_number)

# 4. 범위
max_value = max(integers)
min_value = min(integers)
print(max_value - min_value)