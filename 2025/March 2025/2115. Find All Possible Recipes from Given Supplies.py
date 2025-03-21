from collections import deque
class Solution:
    def findAllRecipes(self, recipes, ingredients, supplies):
        avail, q, res = set(supplies), deque(range(len(recipes))), []
        last = -1
        while len(avail) > last:
            last, size = len(avail), len(q)
            for _ in range(size):
                i = q.popleft()
                if all(item in avail for item in ingredients[i]):
                    avail.add(recipes[i])
                    res.append(recipes[i])
                else:
                    q.append(i)
        return res
