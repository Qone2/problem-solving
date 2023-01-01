import math


ans_dict = dict()
answer = 0
N = 0
number_list = []
is_used = list()


def solution(numbers):
    global answer
    global N
    global number_list
    global is_used
    N = len(numbers)
    number_list = numbers
    is_used = list(False for _ in range(N))

    permutation(0, '')

    return answer


def is_prime(number):
    if number <= 1:
        return False

    sq_num = math.sqrt(number)
    i = 2
    while i <= sq_num:
        if number % i == 0:
            return False
        i += 1

    return True


def permutation(depth, number):
    global answer
    global N
    global number_list
    global is_used
    try:
        real_number = int(number)
    except:
        real_number = 0
    print(number)
    if not ans_dict.get(real_number) and is_prime(real_number):
        answer += 1
        ans_dict[real_number] = True

    if depth == N:
        return

    for i in range(N):
        if is_used[i] is True:
            continue

        is_used[i] = True
        permutation(depth + 1, number + number_list[i])
        is_used[i] = False


if __name__ == "__main__":
    print(solution("17"))
