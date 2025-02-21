class FindElements:
    def __init__(self, root: TreeNode):
        self.seen = set()
        self._recover(root, 0)

    def find(self, target: int) -> bool:
        return target in self.seen

    def _recover(self, node, val):
        if not node:
            return
        self.seen.add(val)
        self._recover(node.left, val * 2 + 1)
        self._recover(node.right, val * 2 + 2)
