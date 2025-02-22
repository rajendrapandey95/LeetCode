class Solution:
    def __init__(self):
        self.i = 0  # Shortened index variable

    def recoverFromPreorder(self, traversal: str) -> TreeNode:
        return self._build(traversal, 0)

    def _build(self, s, depth):
        if self.i >= len(s):
            return None

        dashes = 0
        while self.i + dashes < len(s) and s[self.i + dashes] == "-":
            dashes += 1

        if dashes != depth:
            return None

        self.i += dashes
        value = 0
        while self.i < len(s) and s[self.i].isdigit():
            value = value * 10 + int(s[self.i])
            self.i += 1

        node = TreeNode(value)
        node.left = self._build(s, depth + 1)
        node.right = self._build(s, depth + 1)

        return node
