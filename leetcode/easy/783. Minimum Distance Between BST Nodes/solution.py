from typing import *
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left: TreeNode = left
        self.right: TreeNode = right


class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        queue: Deque[TreeNode] = deque()
        min_d = 1234567890
        queue.append(root)
        node_list = []

        while queue:
            node = queue.popleft()
            node_list.append(node.val)
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)

        node_list.sort()
        for i in range(len(node_list) - 1):
            min_d = min(min_d, node_list[i + 1] - node_list[i])

        return min_d
