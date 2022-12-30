from typing import *
from collections import deque


def solution(begin: str, target: str, words: List[str]) -> int:
    """
    가능한 모든 글자들 중에서 방문하지 않았고 한글자 차이인 글자들에 대하여 bfs탐색
    방문여부를 전체로 봐야할까 현재 순회를 기준으로 봐야할까
    """
    answer = 0
    # 큐 선언 (현재단어와 경로, 걸음 수를 포함)
    queue: Deque[Tuple[str, List[str], int]] = deque()
    # 방문여부 선언
    visited = list(False for _ in range(len(words)))
    # 큐에 시작단어 삽입
    queue.append((begin, [], 0))
    # 큐가 빌때까지
    while queue:
        # pop하고
        current_str, path, step = queue.popleft()
        # 종료 조건
        if current_str == target:
            return step
        # 모든 words에 대하여 후보인것들 방문 처리 후 path복사 후 추가하고 큐에 삽입
        for i, w in enumerate(words):
            if is_diff_one(current_str, w) and visited[i] is False:
                visited[i] = True
                new_path = path[:]
                new_path.append(w)
                queue.append((w, new_path, step + 1))

    return 0


def is_diff_one(s1: str, s2: str) -> bool:
    count = 0
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            count += 1
    return count == 1


if __name__ == "__main__":
    print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))
    print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log"]))
