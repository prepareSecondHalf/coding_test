# stack 생성
stack = []

# stack에 데이터 삽입
stack.append(5)
stack.append(2)
stack.append(3)
stack.append(7)
# stack에 데이터 꺼내기
stack.pop()
stack.append(1)
stack.append(4)
stack.pop()

# stack 데이터를 순서대로 출력
print(stack)
# stack 데이터를 맨 뒤 순서대로 출력
print(stack[::-1])
# stack 데이터를 맨 뒤 데이터만 출력
print(stack[-1::])