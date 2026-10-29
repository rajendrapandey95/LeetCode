class Tree:
    def __init__(self, n: int, edges: list[list[int]]):
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        parent, tin, tout, order = [0] * n, [0] * n, [0] * n, []
        stack = [0]
        while stack:
            x = stack.pop()
            if x < 0:
                tout[~x] = len(order)
                continue
            tin[x] = len(order)
            order.append(x)
            stack.append(~x)
            for y in graph[x]:
                if y != parent[x]:
                    parent[y] = x
                    stack.append(y)

        first = [[tin[parent[x]] for x in order]]
        for k in range(1, n.bit_length()):
            prev = first[-1]
            first.append([*map(min, prev, prev[1 << k - 1:])])
        self.parent, self.tin, self.tout, self.order, self.first = parent, tin, tout, order, first

    def lca(self, u: int, v: int) -> int:
        if u == v:
            return u
        l, r = sorted((self.tin[u], self.tin[v]))
        k = (r - l).bit_length() - 1
        return self.order[min(self.first[k][l + 1], self.first[k][r - (1 << k) + 1])]


class RootPaths:
    def __init__(self, tree: Tree, bit: list[int]):
        self.start = start = bit[:]
        for x in tree.order[1:]:
            start[x] ^= start[tree.parent[x]]
        self.tin, self.tout = tree.tin, tree.tout
        self.fenwick = [0] * (len(bit) + 1)

    def flip(self, x: int, d: int):
        fenwick = self.fenwick
        for i in self.tin[x] + 1, self.tout[x] + 1:
            while i < len(fenwick):
                fenwick[i] ^= d
                i += i & -i

    def __getitem__(self, x: int) -> int:
        fenwick, mask, i = self.fenwick, self.start[x], self.tin[x] + 1
        while i:
            mask ^= fenwick[i]
            i -= i & -i
        return mask


class Solution:
    def palindromePath(self, n: int, edges: list[list[int]], s: str, queries: list[str]) -> list[bool]:
        tree = Tree(n, edges)
        bit = [1 << ord(c) - 97 for c in s]
        paths = RootPaths(tree, bit)

        ans = []
        for q in queries:
            kind, a, b = q.split()
            if kind == 'update':
                x, new_bit = int(a), 1 << ord(b) - 97
                paths.flip(x, bit[x] ^ new_bit)
                bit[x] = new_bit
            else:
                u, v = int(a), int(b)
                mask = paths[u] ^ paths[v] ^ bit[tree.lca(u, v)]
                ans.append(mask.bit_count() <= 1)
        return ans
