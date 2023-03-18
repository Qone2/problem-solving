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
    N = int(input())
    nums = list(map(int, input().split()))
    count = 0
    for n in nums:
        if is_prime(n):
            count += 1
    print(count)
