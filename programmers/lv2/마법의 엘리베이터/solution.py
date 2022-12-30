import math


def solution(storey: int) -> int:
    """
    각 자릿수 숫자로 나누고, 소숫점 첫번째 자리에서 반올림 한 값을 더해주는 식으로
    다만 반올림을 할때 소숫점 첫번째가 5면 그 다음 자릿수가 5보다 큰지를 봐야한다.
    다음 자릿수도 5인 경우 재귀적으로 처리
    """
    answer = 0
    # 자릿수별로
    for i in range(len(str(storey)), -1, -1):
        # 자릿수 만큼 나누고 반올림
        rounded = 0
        if is_floor(storey, i):
            rounded = math.floor(storey / (10 ** i))
        else:
            rounded = math.ceil(storey / (10 ** i))
        answer += rounded
        storey = abs(storey - 10 ** i * rounded)

    return answer


def is_floor(storey, i) -> bool:
    # 555등의 경우 예외
    is_all_five = True
    for c in str(storey):
        if c != '5':
            is_all_five = False
    if is_all_five and len(str(storey)) > 2:
        return False

    if storey % (10 ** i) // (10 ** (i - 1)) < 5:
        return True
    elif storey % (10 ** i) // (10 ** (i - 1)) > 5:
        return False
    else:
        return is_floor(storey, i - 1)


if __name__ == "__main__":
    print(solution(2554))
    print(solution(16))
    print(solution(15))
    print(f"{25} = {solution(25)}")
    print(f"{95} = {solution(95)}")
    print(f"{55} = {solution(55)}")
    print(f"{105} = {solution(105)}")
    print(f"{1000} = {solution(1000)}")
    print(f"{1523} = {solution(1523)}")
    print(f"{157} = {solution(157)}")
    print(f"{155} = {solution(155)}")
    print(f"{1557} = {solution(1557)}")
    print(f"{955555} = {solution(955555)}")
    print(f"{335555} = {solution(335555)}")
    print(f"{5555} = {solution(5555)}")
    print(f"{15555} = {solution(15555)}")
