str = input()

for i in range(ord('a'), ord('z')+1):
    print(str.find(chr(i)), end=" ")