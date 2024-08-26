# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:
    def postorder(self, rt: 'Node') -> List[int]:
        res = []

        if not rt:
            return res

        stk = [rt]

        while stk:
            nd = stk.pop()
            res.append(nd.val)
            stk.extend(nd.children)  # Adding children to the stack

        res.reverse()
        return res
