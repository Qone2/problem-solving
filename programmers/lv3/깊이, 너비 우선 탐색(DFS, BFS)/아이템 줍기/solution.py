from collections import deque
from typing import *


def solution(rectangle: List[List[int]], characterX: int, characterY: int, itemX: int, itemY: int) -> int:
    """
    기본적인 아이디어는 전체 사각형들을 아우르는 지도에서 길찾기를 하는 것과 같음
    그저 유효한 길인지 판정하는 함수만 추가로 필요
    """
    answer = 0
    # 전체 지도는 (0, 0) 부터 가장 큰(x, y)
    max_x, max_y = 0, 0
    for r in rectangle:
        if max_x < r[2]:
            max_x = r[2]
        if max_y < r[3]:
            max_y = r[3]
    # 방문 여부를 그에 맞게 제작
    visited = list(list(False for _ in range(max_y + 1)) for _ in range(max_x + 1))
    # dx, dy 선언
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    # 큐 선언
    queue: Deque[Tuple[int, int, int]] = deque()
    # 시작점, 카운트 방문처리 후 큐에 삽입
    visited[characterX][characterY] = True
    queue.append((characterX, characterY, 0))
    # 큐가 빌때까지
    while queue:
        # 팝 하고 조건 확인
        x, y, count = queue.popleft()
        if x == itemX and y == itemY:
            return count
        # 주변에 대하여 조건 만족하면 bfs
        for i in range(len(dx)):
            nx = x + dx[i]
            ny = y + dy[i]
            hx = x + dx[i] / 2
            hy = y + dy[i] / 2
            if (is_valid(rectangle, nx, ny) and visited[nx][ny] is False) and (
                    is_valid(rectangle, hx, hy)):
                visited[nx][ny] = True
                queue.append((nx, ny, count + 1))

    return answer


def is_valid(rectangle: List[List[int]], m: int, n: int) -> bool:
    """
    선위에 있어야 하며 그 어떤 사각형의 안쪽에 있어선 안된다.
    """
    return is_online(rectangle, m, n) and not is_inline(rectangle, m, n)


def is_online(rectangle: List[List[int]], m: int, n: int) -> bool:
    on_line = False
    for r in rectangle:
        if (m == r[0] and r[1] <= n <= r[3]) or (n == r[1] and r[0] <= m <= r[2]) or (
                n == r[3] and r[0] <= m <= r[2]) or (m == r[2] and r[1] <= n <= r[3]):
            on_line = True
            break
    return on_line


def is_inline(rectangle: List[List[int]], m: int, n: int) -> bool:
    in_line = False
    for r in rectangle:
        if (r[0] < m < r[2]) and (r[1] < n < r[3]):
            in_line = True
            break
    return in_line


def same_rect(rectangle: List[List[int]], x, y, nx, ny) -> bool:
    set1 = set()
    set2 = set()
    for r in rectangle:
        if is_online([r], x, y):
            set1.add((r[0], r[1], r[2], r[3]))
        if is_online([r], nx, ny):
            set2.add((r[0], r[1], r[2], r[3]))
    return len(set1.intersection(set2)) > 0


if __name__ == "__main__":
    print(solution([[1, 1, 7, 4], [3, 2, 5, 5], [4, 3, 6, 9], [2, 6, 8, 8]], 1, 3, 7, 8))
    print(solution([[1, 1, 8, 4], [2, 2, 4, 9], [3, 6, 9, 8], [6, 3, 7, 7]], 9, 7, 6, 1))
    print(solution([[1, 1, 5, 7]], 1, 1, 4, 7))
    print(solution([[2, 1, 7, 5], [6, 4, 10, 10]], 3, 1, 7, 10))
    print(solution([[2, 2, 5, 5], [1, 3, 6, 4], [3, 1, 4, 6]], 1, 4, 6, 3))
