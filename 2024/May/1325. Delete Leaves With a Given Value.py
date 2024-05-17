# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        def delete_target_leaves(node: Optional[TreeNode]) -> Optional[TreeNode]:
            if not node:
                return None
            node.left = delete_target_leaves(node.left)
            node.right = delete_target_leaves(node.right)
            if node.left is None and node.right is None and node.val == target:
                return None
            return node
        return delete_target_leaves(root)
