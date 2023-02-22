import sys

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

inp_arr = list(str(sys.stdin.readline()))

for i in range(len(alphabet)):
    if alphabet[i] in inp_arr:
        alphabet[i] = str(inp_arr.index(alphabet[i]))
    else:
        alphabet[i] = "-1"
        
result = " ".join(alphabet)
print(result)