from collections import deque
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        queue = deque([root])
        level = 0
        
        while queue:
            size = len(queue)
            prev_val = None if level % 2 == 0 else float('inf')
            
            for _ in range(size):
                node = queue.popleft()
                
                # Check if current node's value meets the criteria
                if level % 2 == 0:  # Even level
                    if node.val % 2 == 0 or (prev_val is not None and prev_val >= node.val):
                        return False
                else:  # Odd level
                    if node.val % 2 != 0 or (prev_val is not None and prev_val <= node.val):
                        return False
                
                prev_val = node.val
                
                # Add children to the queue
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            level += 1
        
        return True
