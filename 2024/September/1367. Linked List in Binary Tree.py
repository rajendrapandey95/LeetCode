class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        if not root:
            return False
        return self._check_path(root, head)

    def _check_path(self, node: Optional[TreeNode], head: Optional[ListNode]) -> bool:
        if not node:
            return False
        if self._dfs(node, head):
            return True
        return self._check_path(node.left, head) or self._check_path(node.right, head)

    def _dfs(self, node: Optional[TreeNode], head: Optional[ListNode]) -> bool:
        if not head:
            return True
        if not node or node.val != head.val:
            return False
        return self._dfs(node.left, head.next) or self._dfs(node.right, head.next)
