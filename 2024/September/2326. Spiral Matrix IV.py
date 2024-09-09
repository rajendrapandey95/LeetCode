class Solution:
    def spiralMatrix(self, m: int, n: int, head: "ListNode") -> List[List[int]]:
        i, j, cur_d = 0, 0, 0
        movement = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        res = [[-1] * n for _ in range(m)]
        
        while head:
            res[i][j] = head.val
            ni, nj = i + movement[cur_d][0], j + movement[cur_d][1]

            if not (0 <= ni < m and 0 <= nj < n and res[ni][nj] == -1):
                cur_d = (cur_d + 1) % 4
            
            i += movement[cur_d][0]
            j += movement[cur_d][1]
            head = head.next
        
        return res
