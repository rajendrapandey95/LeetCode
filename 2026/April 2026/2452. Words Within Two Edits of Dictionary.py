class Solution:
    def twoEditWords(self, queries, dictionary):
        ans = []
        for q in queries:
            for w in dictionary:
                diff = 0
                for a, b in zip(q, w):
                    if a != b:
                        diff += 1
                        if diff > 2:
                            break
                if diff <= 2:
                    ans.append(q)
                    break
        return ans
