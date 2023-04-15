'''
  수열을 내림차순 정렬

  수도코드
  n = 입력 받는 값의 갯수
  나머지 입력값 = n만큼의 str값

  빈 리스트 생성
  n개의 길이만큼 입력값을 받는다
  받은 값을 리스트에 추가한다
  추가한 리스트를 내림차순으로 정렬한다
  - 내림차순 정렬은 정렬 함수인 sort 또는 sorted 라이브러리를 사용한다
  정렬처리된 리스트를 출력한다
  - 다만, 출력할 때마다 공백을 추가한다
'''
array = []
n = int(input())

for _ in range(n):
  array.append(int(input()))
# array = array.sort() -> 정렬 후 array를 출력하면, None 값이 출력된다. why?
array = sorted(array, reverse=True)

for num in array:
  print(num, end=" ")
