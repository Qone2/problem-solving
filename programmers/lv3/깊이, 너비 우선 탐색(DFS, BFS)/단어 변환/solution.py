from collections import deque


def solution(begin, target, words):
    answer = 0
    if target not in words:
        return 0
    visited = list(False for _ in range(len(words)))
    answer = bfs(words, begin, visited, target)

    return answer


def bfs(words: list, start: str, visited: list, target: str):
    queue = deque([(start, 0)])
    while queue:
        v, move = queue.popleft()
        if v == target:
            return move
        print(v)
        for i, word in enumerate(words):
            if visited[i] is False and diff(word, v) == 1:
                queue.append((word, move + 1))
                visited[i] = True


def diff(str1: str, str2: str):
    dif_val = 0
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            dif_val += 1
    return dif_val


if __name__ == "__main__":
    print(diff("hit", "hot"))
    print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))
    print(solution("hit", "cog", ["hot", "lot", "dog", "dot", "log", "cog"]))
