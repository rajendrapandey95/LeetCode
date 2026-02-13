class Solution:
    def longestBalanced(self, s: str) -> int:
        c = list(s)
        n = len(c)

        cur_a = cur_b = cur_c = 0
        max_a = max_b = max_c = 0

        for i in range(n):
            if c[i] == 'a':
                cur_a = cur_a + 1 if i > 0 and c[i-1] == 'a' else 1
                max_a = max(max_a, cur_a)
            elif c[i] == 'b':
                cur_b = cur_b + 1 if i > 0 and c[i-1] == 'b' else 1
                max_b = max(max_b, cur_b)
            else:
                cur_c = cur_c + 1 if i > 0 and c[i-1] == 'c' else 1
                max_c = max(max_c, cur_c)

        res = max(max_a, max_b, max_c)

        res = max(res, self.find2(c, 'a', 'b'))
        res = max(res, self.find2(c, 'a', 'c'))
        res = max(res, self.find2(c, 'b', 'c'))

        res = max(res, self.find3(c))

        return res

    def find2(self, c, x, y):
        n = len(c)
        max_len = 0

        first = [-2] * (2 * n + 1)
        clear_idx = -1
        diff = n
        first[diff] = -1

        for i in range(n):
            if c[i] != x and c[i] != y:
                clear_idx = i
                diff = n
                first[diff] = clear_idx
            else:
                if c[i] == x:
                    diff += 1
                else:
                    diff -= 1

                if first[diff] < clear_idx:
                    first[diff] = i
                else:
                    max_len = max(max_len, i - first[diff])

        return max_len

    def find3(self, c):
        state = 10**18 
        first = {state: -1}

        max_len = 0

        for i in range(len(c)):
            if c[i] == 'a':
                state += 1_000_001
            elif c[i] == 'b':
                state -= 1_000_000
            else:
                state -= 1

            if state in first:
                max_len = max(max_len, i - first[state])
            else:
                first[state] = i

        return max_len
