from collections import deque
from typing import *


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        queue: Deque[TreeNode] = deque()
        queue.append(root)

        while queue:
            node = queue.popleft()
            if node is None:
                continue
            tmp = node.left
            node.left = node.right
            node.right = tmp
            queue.append(node.right)
            queue.append(node.left)

        return root
