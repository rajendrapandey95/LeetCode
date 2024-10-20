from collections import deque

class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        st = deque()
        for c in expression:
            if c in [",", "("]:
                continue
            if c in "tf!&|":
                st.append(c)
            elif c == ")":
                has_true, has_false = False, False
                while st[-1] not in "!&|":
                    top_value = st.pop()
                    has_true |= (top_value == "t")
                    has_false |= (top_value == "f")
                op = st.pop()
                if op == "!":
                    st.append("t" if not has_true else "f")
                elif op == "&":
                    st.append("f" if has_false else "t")
                else:
                    st.append("t" if has_true else "f")
        return st[-1] == "t"
