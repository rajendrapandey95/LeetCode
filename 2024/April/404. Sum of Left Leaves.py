# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        def is_leaf(node):
            return node and not node.left and not node.right
        
        def dfs(node, is_left):
            if not node:
                return 0
            
            if is_leaf(node) and is_left:
                return node.val
            
            left_sum = dfs(node.left, True)
            right_sum = dfs(node.right, False)
            
            return left_sum + right_sum
        
        return dfs(root, False)
