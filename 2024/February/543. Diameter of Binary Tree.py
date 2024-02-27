# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # Helper function to calculate the diameter and depth of the tree
        def dfs(node):
            nonlocal max_diameter
            if not node:
                return 0
            left_depth = dfs(node.left)
            right_depth = dfs(node.right)
            max_diameter = max(max_diameter, left_depth + right_depth)
            return 1 + max(left_depth, right_depth)
        
        max_diameter = 0
        dfs(root)
        return max_diameter
