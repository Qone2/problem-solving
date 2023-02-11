from typing import *
from collections import deque


class Solution:
    # 힌트 참조
    def maxDistance(self, grid: List[List[int]]) -> int:
        max_count = 0
        not_one = True
        not_zero = True
        visited = list(list(False for _ in range(len(grid[0]))) for _ in range(len(grid)))
        for n in range(len(grid)):
            for m in range(len(grid[0])):
                max_count = max(max_count, self.bfs(n, m, grid, visited))
                if grid[n][m] == 1:
                    not_one = False
                if grid[n][m] == 0:
                    not_zero = False
        if not_zero:
            return -1
        return max_count if not not_one else -1

    def bfs(self, x: int, y: int, grid: List[List[int]], visited):
        queue = deque()
        visited = list(list(False for _ in range(len(grid[0]))) for _ in range(len(grid)))
        if grid[x][y] == 1:
            return 0
        visited[x][y] = True
        queue.append((x, y, 0))
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]
        count = 0
        while queue:
            x, y, count = queue.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and not visited[nx][ny]:
                    if grid[nx][ny] == 1:
                        return count + 1
                    visited[nx][ny] = True
                    queue.append((nx, ny, count + 1))
        return count


if __name__ == "__main__":
    sol = Solution()
    print(sol.maxDistance([[1, 0, 1], [0, 0, 0], [1, 0, 1]]))
