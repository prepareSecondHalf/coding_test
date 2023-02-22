import sys

a = sys.stdin.readline()

if type(a) is int:
    print(chr(a))
else:
    print(ord(a))