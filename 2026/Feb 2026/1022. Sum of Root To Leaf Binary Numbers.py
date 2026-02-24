class Solution:
    def sumRootToLeaf(self, root):
        def f(n, v):
            if not n: return 0
            v = (v<<1) | n.val
            return v if not n.left and not n.right else f(n.left,v)+f(n.right,v)
        return f(root,0)
