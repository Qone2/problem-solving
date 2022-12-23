def solution(t, p):
    answer = 0
    int_p = int(p)
    # for i 순회
    for i in range(len(t) - len(p) + 1):
        # int 부분문자열 < int(p)이면 answer + 1
        if int(t[i:i + len(p)]) <= int_p:
            answer += 1

    return answer


if __name__ == "__main__":
    print(solution("3141592", "271"))
    print(solution("500220839878", "7"))
