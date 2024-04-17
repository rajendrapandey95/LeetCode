class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        smallest_string = ""
        node_queue = deque()
        node_queue.append([root, chr(root.val + ord('a'))])
        while node_queue:
            node, current_string = node_queue.popleft()
            if not node.left and not node.right:
                smallest_string = min(smallest_string, current_string) if smallest_string else current_string
            if node.left:
                node_queue.append([node.left, chr(node.left.val + ord('a')) + current_string])
            if node.right:
                node_queue.append([node.right, chr(node.right.val + ord('a')) + current_string])
        return smallest_string
