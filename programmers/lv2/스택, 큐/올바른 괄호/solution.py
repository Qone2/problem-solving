def solution(string: str):
    # 스택을 선언
    stack = []
    # 문자에 대하여 for
    for s in string:
        # '('이면 스택에 넣고
        if s == '(':
            stack.append(s)
        # ')'이면 스택에서 뺀다 빼는게 불가능 하면 return false
        elif s == ')':
            if len(stack) < 1:
                return False
            stack.pop()
        else:
            return False

    # for문 종료 후 스택에 남은게 없으면 return true 있으면 false
    return len(stack) == 0
