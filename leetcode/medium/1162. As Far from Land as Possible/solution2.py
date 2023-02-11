from typing import *
from collections import deque


class Solution:
    # 답변 참조
    def maxDistance(self, grid: List[List[int]]) -> int:
        visited = list(grid[i][:] for i in range(len(grid)))
        queue: Deque[Tuple[int, int]] = deque()
        all_zero = True
        all_one = True
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if visited[i][j] == 1:
                    queue.append((i, j))
                    all_zero = False
                else:
                    all_one = False
        if all_one or all_zero:
            return -1

        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]
        count = -1

        while queue:
            onetime_queue_size = len(queue)
            while onetime_queue_size > 0:
                x, y = queue.popleft()
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and visited[nx][ny] == 0:
                        visited[nx][ny] = 1
                        queue.append((nx, ny))
                onetime_queue_size -= 1
            count += 1

        return count


if __name__ == "__main__":
    sol = Solution()
    print(sol.maxDistance([[1, 0, 1], [0, 0, 0], [1, 0, 1]]))
    print(sol.maxDistance([[1, 1, 1], [1, 1, 1], [1, 1, 1]]))
