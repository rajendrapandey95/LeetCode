class Solution(object):
    def maxNumEdgesToRemove(self, n, edges):
        class UF:
            def __init__(self, n):
                self.rep = list(range(n + 1))
                self.size = [1] * (n + 1)
                self.count = n
            
            def find(self, x):
                if self.rep[x] == x:
                    return x
                self.rep[x] = self.find(self.rep[x])
                return self.rep[x]
            
            def union(self, x, y):
                xr = self.find(x)
                yr = self.find(y)
                
                if xr == yr:
                    return 0
                
                if self.size[xr] > self.size[yr]:
                    self.size[xr] += self.size[yr]
                    self.rep[yr] = xr
                else:
                    self.size[yr] += self.size[xr]
                    self.rep[xr] = yr
                
                self.count -= 1
                return 1
            
            def connected(self):
                return self.count == 1
    
        alice = UF(n)
        bob = UF(n)
        
        edges_needed = 0
        
        for edge in edges:
            if edge[0] == 3:
                edges_needed += (alice.union(edge[1], edge[2]) | bob.union(edge[1], edge[2]))
        
        for edge in edges:
            if edge[0] == 2:
                edges_needed += bob.union(edge[1], edge[2])
            elif edge[0] == 1:
                edges_needed += alice.union(edge[1], edge[2])
        
        if alice.connected() and bob.connected():
            return len(edges) - edges_needed
        
        return -1
