from typing import Optional

class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        MOD = 10**9 + 7
        subsums = []

        def dfs(node):
            if not node:
                return 0
            s = node.val + dfs(node.left) + dfs(node.right)
            subsums.append(s)
            return s

        total = dfs(root)

        return max(s * (total - s) for s in subsums) % MOD
