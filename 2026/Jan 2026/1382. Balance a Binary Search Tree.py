class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        arr = []

        def inorder(node):
            if not node:
                return
            inorder(node.left)
            arr.append(node.val)
            inorder(node.right)

        def build(l, r):
            if l > r:
                return None
            m = (l + r) // 2
            return TreeNode(arr[m], build(l, m - 1), build(m + 1, r))

        inorder(root)
        return build(0, len(arr) - 1)
