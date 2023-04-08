# 카카오 신입공채 1차, programmers.co.kr/learn/courses/30/lessons/60058

def solution(p):
    answer = ''
    if isCorrect(p): return p
    answer = rec(p)
    return answer


def sepUV(p): 
    # 균형잡힌 괄호 문자열이 등장하면 그 부분까지 쪼갠다
    left, right = 0, 0
    for i in range(len(p)):
        if p[i] == '(':
            left += 1
        else:
            right += 1
        if left == right:
            u = p[:i + 1]
            v = p[i + 1:] if i + 1 < len(p) else ""
            break
    return u, v

# 올바른 문자열인가를 판단하는 함수
def isCorrect(p):
    stack = []
    # (가 있으면 stack에 추가 )가 나오면 False 리턴
    for c in p:
        if c == '(':
            stack.append(c)
        else:
            if not len(stack):
                return False
            elif stack[-1] == '(':
                stack.pop()
    return False if len(stack) else True


def rec(p):
    result = ""
    if not len(p): return ""
    # sepUV(p) 실행 u = p[:i + 1] v = p[i + 1:] 리턴
    u, v = sepUV(p)
    # isCorrect(u)로 올바른 문자열인지 판단후 재귀함수 실행 False가 나오면 올바른 괄호 문자열로 수정후 리턴
    if isCorrect(u):
        result = u + rec(v)
    else:
        tmp = "("
        tmp += rec(v)
        tmp += ")"
        u = u[1:-1]
        for c in u:
            if c == '(':
                tmp += ')'
            else:
                tmp += '('
        result += tmp
    return result