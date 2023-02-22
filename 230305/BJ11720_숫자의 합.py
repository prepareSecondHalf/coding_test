# N개의 숫자가 공백 없이 쓰여있다. 이 숫자를 모두 합해서 출력하는 프로그램을 작성하시오.
# 첫째 줄에 숫자의 개수 N (1 ≤ N ≤ 100)이 주어진다. 둘째 줄에 숫자 N개가 공백없이 주어진다.
# 입력으로 주어진 숫자 N개의 합을 출력한다.

number_of_numbers = int(input())
strs = list(input())
nums = [int(x) for x in strs]
print(sum(nums))

# 질문: 테스트는 통과하는데 첫째 줄에서 입력 받는 숫자의 개수는 의미가 없어 보이는데?