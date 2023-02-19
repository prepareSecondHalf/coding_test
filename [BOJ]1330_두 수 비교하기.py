input_data = input().split(' ')
a = int(input_data[0])
b = int(input_data[1])

if a > b: 
  print('>')
elif a < b:
  print('<')
else:
  print('==')