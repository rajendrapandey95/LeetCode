class Solution:
    def pyramidTransition(self, bottom, allowed):
        T = [[0] * 128 for _ in range(128)]

        for a, b, c in allowed:
            u, v, w = 1 << (ord(a)-65), 1 << (ord(b)-65), 1 << (ord(c)-65)
            for i in range(128):
                if i & u:
                    for j in range(128):
                        if j & v:
                            T[i][j] |= w

        state = [1 << (ord(c)-65) for c in bottom]

        while len(state) > 1:
            state = [T[state[i]][state[i+1]] for i in range(len(state)-1)]
            if not any(state):
                return False

        return bool(state[0])
