class Solution:
    def constructFromPrePost(self, pre: List[int], post: List[int]) -> Optional[TreeNode]:
        return self.build(pre, post)

    def build(self, pre, post):
        if not pre:
            return None
        root = TreeNode(pre[0])
        if len(pre) == 1:
            return root
        L = post.index(pre[1]) + 1
        root.left = self.build(pre[1:L+1], post[:L])
        root.right = self.build(pre[L+1:], post[L:-1])
        return root
