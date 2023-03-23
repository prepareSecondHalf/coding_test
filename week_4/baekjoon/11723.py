import sys

N = int(sys.stdin.readline())

def calculate(arr, calc, num):
    result = arr

    if calc == 'add':
        result.add(num)
    elif calc == 'remove':
        if num in result:
            result.remove(num)
    elif calc == 'check':
        if num in result:
            print(1)
        else:
            print(0)
    elif calc == 'toggle':
        if num in result:
            result.remove(num)
        else:
            result.add(num)
    elif calc == 'all':
        result = set([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])
    else:
        result = set([])
    
    return result
    
result = set([])

for i in range(N):
    calc, num = sys.stdin.readline().strip().split()

    result = calculate(result, calc, int(num))