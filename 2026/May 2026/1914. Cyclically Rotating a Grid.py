class Solution:
    def rotateGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        nlayer = min(m // 2, n // 2)  
        for layer in range(nlayer):
            r = []
            c = []  
            val = []  
            for i in range(layer, m - layer - 1):  
                r.append(i)
                c.append(layer)
                val.append(grid[i][layer])
            for j in range(layer, n - layer - 1): 
                r.append(m - layer - 1)
                c.append(j)
                val.append(grid[m - layer - 1][j])
            for i in range(m - layer - 1, layer, -1):
                r.append(i)
                c.append(n - layer - 1)
                val.append(grid[i][n - layer - 1])
            for j in range(n - layer - 1, layer, -1): 
                r.append(layer)
                c.append(j)
                val.append(grid[layer][j])
            total = len(val)  
            kk = k % total  
            
            for i in range(total):
                idx = (
                    i + total - kk
                ) % total  
                grid[r[i]][c[i]] = val[idx]
        return grid
