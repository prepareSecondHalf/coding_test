# s의 
def solution(s):
    if len(s) == 1:
        return 1
    
    # 1, 2, 3, 4, ... 개로 문자열 나눴을 때 길이
    lenArr = []

    # 길이의 반까지만 테스트하면 됨 -> 반 넘어가면 중복 없음
    for i in range(1, len(s) // 2 + 1):
        # 1, 2, 3, 4, ...개로 나눠서 들어갈 단어들
        splitedArr = []

        for j in range(0, len(s), i):
            splitedArr.append(s[j:j + i])

        dupliCnt = 1 # 중복 갯수
        currentElement = splitedArr[0]
        sentence = '' # 만들어질 문장

        for k in range(1, len(splitedArr)):
            if currentElement != splitedArr[k]:
                if dupliCnt != 1:
                    sentence += str(dupliCnt)
                sentence += currentElement

                dupliCnt = 1
                currentElement = splitedArr[k]
            else:
                dupliCnt += 1

            if k == len(splitedArr) - 1: # 마지막 단어에 대해
                if dupliCnt != 1:
                    sentence += str(dupliCnt)
                    sentence += currentElement
                else:
                    sentence += splitedArr[k]

        lenArr.append(len(sentence))

    return min(lenArr)