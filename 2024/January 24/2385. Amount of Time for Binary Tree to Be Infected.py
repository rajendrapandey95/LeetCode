# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.maxDistance = 0

    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        self.traverse(root, start)
        return self.maxDistance

    def traverse(self, root: Optional[TreeNode], start: int) -> int:
        depth = 0
        if not root:
            return depth

        leftDepth = self.traverse(root.left, start)
        rightDepth = self.traverse(root.right, start)

        if root.val == start:
            self.maxDistance = max(leftDepth, rightDepth)
            depth = -1
        elif leftDepth >= 0 and rightDepth >= 0:
            depth = max(leftDepth, rightDepth) + 1
        else:
            distance = abs(leftDepth) + abs(rightDepth)
            self.maxDistance = max(self.maxDistance, distance)
            depth = min(leftDepth, rightDepth) - 1

        return depth
