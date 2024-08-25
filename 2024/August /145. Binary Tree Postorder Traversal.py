class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        def dfs(node):
            if not node: return
            dfs(node.left)
            dfs(node.right)
            res.append(node.val)
        dfs(root)
        return res
