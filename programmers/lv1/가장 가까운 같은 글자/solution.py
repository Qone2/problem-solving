def solution(s):
    answer = []
    # 딕셔너리 선언
    my_map = {}
    # s 순회
    for i, c in enumerate(s):
        # 글자가 전에 있었다면 그때의 인덱스 기록
        if c in my_map:
            # 이전 값의 인덱스차 기록
            answer.append(i - my_map[c])
            my_map[c] = i
        else:
            # 처음 글자면 -1 기록
            answer.append(-1)
            my_map[c] = i

    return answer
