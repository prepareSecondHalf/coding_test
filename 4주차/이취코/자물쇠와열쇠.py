
def rotate(key):
    m = len(key)
    result = [[0] * m for _ in range(m)]
    for i in range(m):
        for j in range(m):
            result[j][m - 1 - i] = key[i][j]
    return result


def check(lock_padding):
    lock_length = len(lock_padding) // 3
    for i in range(lock_length, lock_length*2):
        for j in range(lock_length, lock_length*2):
            if lock_padding[i][j] != 1:
                return False
    return True


def keyIn(lock_padding, key):
    n = len(lock_padding) // 3
    for x in range(n*2):
        for y in range(n*2):
            for i in range(len(key)):
                for j in range(len(key)):
                    lock_padding[x + i][y + j] += key[i][j]
            if check(lock_padding) == True:
                return True
            for i in range(len(key)):
                for j in range(len(key)):
                    lock_padding[x + i][y + j] -= key[i][j]
    return False

def solution(key, lock):
    n = len(lock)
    rotate_count = 0
    lock_padding = [[0] * (n*3) for _ in range(n*3)]
    for i in range(n):
        for j in range(n):
            lock_padding[i + n][j + n] = lock[i][j]
    while True:
        answer = keyIn(lock_padding, key)
        if answer or rotate_count == 3:
            break
        else:
            key = rotate(key)
            rotate_count += 1
    return answer