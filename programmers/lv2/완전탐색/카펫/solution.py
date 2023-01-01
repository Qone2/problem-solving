import math


def solution(brown, yellow):
    answer = []
    sq_num = math.sqrt(yellow)
    for i in range(1, int(sq_num) + 1):
        if yellow % i != 0:
            continue

        if (yellow // i * 2) + 4 + (i * 2) == brown:
            answer.append(yellow // i + 2)
            answer.append(i + 2)
            return answer

    return answer


if __name__ == "__main__":
    print(solution(10, 2))
    print(solution(24, 24))
