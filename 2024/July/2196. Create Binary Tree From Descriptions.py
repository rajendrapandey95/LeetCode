class Solution:
    def createBinaryTree(self, desc: list[list[int]]) -> Optional[TreeNode]:
        def build_tree(val):
            node = TreeNode(val)
            if val in child_map:
                if child_map[val][0] is not None:
                    node.left = build_tree(child_map[val][0])
                if child_map[val][1] is not None:
                    node.right = build_tree(child_map[val][1])
            return node

        child_set = set()
        child_map = {}

        for p, c, is_left in desc:
            if p not in child_map:
                child_map[p] = [None, None]
            child_set.add(c)
            child_map[p][0 if is_left else 1] = c

        for p in child_map:
            if p not in child_set:
                root_val = p
                break
                
        return build_tree(root_val)
