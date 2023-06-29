while True:
    try:
        a, b = map(int, input().split())
    except:
        break
    if (a != 0 and b != 0):
        print(a + b)
