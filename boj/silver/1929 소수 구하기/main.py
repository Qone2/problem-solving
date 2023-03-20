import math


def is_prime(num: int):
    result = True
    if num == 1:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            result = False
            break
    return result


if __name__ == "__main__":
    M, N = map(int, input().split())
    for n in range(M, N + 1):
        if is_prime(n):
            print(n)
