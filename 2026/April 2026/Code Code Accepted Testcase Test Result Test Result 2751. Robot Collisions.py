class Solution:
    def survivedRobotsHealths(self, pos: List[int], health: List[int], dir: str) -> List[int]:
        n = len(pos)
        idx = list(range(n))
        res = []
        stk = deque()

        idx.sort(key=lambda x: pos[x])

        for cur in idx:
            if dir[cur] == "R":
                stk.append(cur)
            else:
                while stk and health[cur] > 0:
                    top = stk.pop()

                    if health[top] > health[cur]:
                        health[top] -= 1
                        health[cur] = 0
                        stk.append(top)
                    elif health[top] < health[cur]:
                        health[cur] -= 1
                        health[top] = 0
                    else:
                        health[cur] = 0
                        health[top] = 0

        for i in range(n):
            if health[i] > 0:
                res.append(health[i])

        return res
