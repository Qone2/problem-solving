def solution(s, skip, index):
    answer = ''
    skip_map = dict()
    for sk in skip:
        skip_map[ord(sk) - 97] = 1
    for c in s:
        as_num = ord(c) - 97
        count = 0
        while count < index:
            as_num += 1
            as_num = as_num % 26
            if as_num in skip_map:
                continue
            count += 1
        answer += chr(as_num + 97)

    return answer


if __name__ == "__main__":
    print(solution("aukks", "wbqd", 5))
