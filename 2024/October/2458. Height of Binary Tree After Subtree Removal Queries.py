class Solution:
    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:
        max_height_after_removal = [0] * 100001
        self.current_max_height = 0

        def traverse_left_to_right(node, current_height):
            if node:
                max_height_after_removal[node.val] = self.current_max_height
                self.current_max_height = max(self.current_max_height, current_height)
                traverse_left_to_right(node.left, current_height + 1)
                traverse_left_to_right(node.right, current_height + 1)

        def traverse_right_to_left(node, current_height):
            if node:
                max_height_after_removal[node.val] = max(
                    max_height_after_removal[node.val], self.current_max_height
                )
                self.current_max_height = max(current_height, self.current_max_height)
                traverse_right_to_left(node.right, current_height + 1)
                traverse_right_to_left(node.left, current_height + 1)

        traverse_left_to_right(root, 0)
        self.current_max_height = 0
        traverse_right_to_left(root, 0)

        return [max_height_after_removal[q] for q in queries]
