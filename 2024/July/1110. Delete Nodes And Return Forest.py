from typing import Optional, List
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def delNodes(self, root: Optional[TreeNode], to_del: List[int]) -> List[TreeNode]:
        if not root:
            return []

        del_set = set(to_del)
        forest = []
        q = deque([root])

        while q:
            node = q.popleft()

            if node.left:
                q.append(node.left)
                if node.left.val in del_set:
                    node.left = None

            if node.right:
                q.append(node.right)
                if node.right.val in del_set:
                    node.right = None

            if node.val in del_set:
                if node.left:
                    forest.append(node.left)
                if node.right:
                    forest.append(node.right)

        if root.val not in del_set:
            forest.append(root)

        return forest
