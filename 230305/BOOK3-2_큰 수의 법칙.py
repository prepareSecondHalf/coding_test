# 동빈이의 큰 수의 법칙은 다양한 수로 이루어진 배열이 있을 때, 주어진 수들을 M번 더하여 가장 큰 수를 만드는 법칙이다.
# 단, 배열의 특정한 인덱스에 해당하는 수가 연속해서 K번을 초과해서 더해질 수 없는 것이 특징이다.
# 서로 다른 인덱스에 해당하는 수가 같은 경우라도 서로 다른 것으로 간주한다.
# 배열의 크기 N, 숫자가 더해지는 횟수 M, K가 주어질 때 동빈이의 큰 수의 법칙에 따른 결과를 출력하시오.
# 첫째 줄에 N(2<=N<=1000), M(1<=N<=10000), K(1<=N<=10000)의 자연수가 주어지며 각 자연수는 공백으로 구분한다.
# 둘째 줄에 N개의 자연수가 주어진다. 각 자연수는 공백으로 구분하며 각 자연수는 1 이상 10000 이하이다.
# K는 항상 M보다 작거나 같다.
# 첫째 줄에 동빈이의 큰 수의 법칙에 따라 더해진 답을 출력한다.

import sys
n, m, k = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))

largest = max(nums)
nums.remove(largest)
second_largest = max(nums)


# 풀이 1
# 가장 큰 수와 두번째로 큰 수의 차이를 구하기(diff)
# 두번째로 큰 수가 들어가는 횟수 구하기(M // K)
# 가장 큰 수 X M에서 diff X M // K
print('first')
diff = largest - second_largest
second_times = m // (k+1)
print((largest * m) - (diff * second_times))


# 풀이 2
# 포인트: 제일 큰 수 찾기, 두번째로 큰 수 찾기
# 배열에서 제일 큰 수를 계속 더한다.
# 이 때, k번 더했으면 k+1번째에서는 두 번째로 큰 수를 더한다.
# 반복한다.
print('second')
sum = 0
times = 0
while times < m:
    times += 1
    if times > k:
        sum += second_largest
        m -= times
        times = 0
    else:
        sum += largest
print(sum)


# 모범답안
