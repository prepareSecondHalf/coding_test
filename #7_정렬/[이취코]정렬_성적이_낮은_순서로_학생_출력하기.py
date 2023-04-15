'''
  n명의 학생 정보
  학생 정보 = 학생 이름, 학생 성적
  성적 낮은 순서대로 학생 이름 출력

  수도코드
  n = 데이터 갯수
  list = 빈 리스트 생성
  n번만큼 입력을 받는다
  - 입력 받을 때마다 list에 값 추가(append)
  리스트 값을 정렬한다
  - 다만, 성적이 낮은 순서라는 조건이 있기 때문에 sorted 함수의 두 번째 인자인 key 속성을 이용한다.
  - key 속성에 대한 함수를 만든다
  정렬한다
  출력한다
'''
n = int(input())
# list = [input() for _ in range(n)] # ['홍길동 95', '이순신 77']와 같이 값이 생성
# list[0], list[1] = [input().split() for _ in range(n)] # TypeError 발생
# list = [input().split() for _ in range(n)] # 이중 리스트 생성됨
arr = []
for _ in range(n):
  item = input().split()
  arr.append((item[0], item[1]))
print(arr)

def setting(data):
  return data[1]
result = sorted(arr, key=setting)
# 혹은 result = sorted(arr, key=lambda student: student[1])

for student_info in result:
  print(student_info[0])
