from collections import deque
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        if not root:
            return -1  # Tree is empty
        
        queue = deque()
        queue.append(root)
        leftmost_value = root.val
        
        while queue:
            level_size = len(queue)
            leftmost_value = queue[0].val  # Update leftmost value for each level
            
            for _ in range(level_size):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        
        return leftmost_value
