import math


def solution(k, d):
    """
    대략적인 풀이방법은 반경 d에 해당하는 원의 각 가능한 y위치에 x를 구하고, 그 라인의 가능한 점 개수를 파악
    """
    answer = 0
    # 가능한 y
    for y in range(0, d + 1, k):
        # 해당 y의 가능한 정수 x 개수 +1은 x = 0인 경우
        answer += int(math.sqrt(d ** 2 - y ** 2)) // k + 1
    return answer


if __name__ == "__main__":
    print(solution(2, 4))
    print(solution(1, 5))
