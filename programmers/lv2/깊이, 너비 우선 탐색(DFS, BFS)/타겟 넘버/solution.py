N = 0
ans = 0


def solution(numbers, target):
    global N
    global ans
    N = len(numbers)
    ans = 0
    dfs(0, 0, target, numbers)

    return ans


def dfs(depth: int, result: int, target: int, numbers: list):
    global N
    global ans
    if depth == N:
        if result == target:
            ans += 1
        return
    else:
        dfs(depth + 1, result + numbers[depth], target, numbers)
        dfs(depth + 1, result - numbers[depth], target, numbers)


if __name__ == "__main__":
    print(solution([1, 1, 1, 1, 1], 3))
    print(solution([4, 1, 2, 1], 4))
    print(solution([4, 1, 2, 1], 4))
