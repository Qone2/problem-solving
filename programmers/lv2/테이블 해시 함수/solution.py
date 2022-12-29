def solution(data, col, row_begin, row_end):
    answer = 0
    sorted_data = sorted(sorted(data, key=lambda x: x[0], reverse=True), key=lambda y: y[col - 1])
    for i in range(row_begin - 1, row_end):
        s = 0
        for j in range(len(data[0])):
            s += sorted_data[i][j] % (i + 1)
        if i == row_begin - 1:
            answer = s
            continue

        answer ^= s

    return answer
