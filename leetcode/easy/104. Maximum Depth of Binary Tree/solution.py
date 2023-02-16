from typing import *
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        queue: Deque[Tuple[TreeNode, int]] = deque()
        if root is None:
            return 0
        queue.append((root, 2))
        max_count = 1

        while queue:
            tmp_node, count = queue.popleft()
            left, right = tmp_node.left, tmp_node.right
            if left is not None:
                max_count = max(max_count, count)
                queue.append((left, count + 1))
            if right is not None:
                max_count = max(max_count, count)
                queue.append((right, count + 1))
        return max_count
