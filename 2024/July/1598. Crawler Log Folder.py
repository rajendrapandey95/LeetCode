class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stk = []

        for op in logs:
            if op == "../":
                if stk:
                    stk.pop()
            elif op != "./":
                stk.append(op)

        return len(stk)
