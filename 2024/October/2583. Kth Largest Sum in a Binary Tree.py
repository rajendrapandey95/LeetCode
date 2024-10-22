class Solution:
    def kthLargestLevelSum(self, root: TreeNode, k: int) -> int:
        pq, bfs_queue = [], deque([root])

        while bfs_queue:
            level_sum = sum(node.val for node in bfs_queue)
            pq.append(-level_sum)

            for _ in range(len(bfs_queue)):
                node = bfs_queue.popleft()
                if node.left: bfs_queue.append(node.left)
                if node.right: bfs_queue.append(node.right)

        if len(pq) < k: return -1
        pq.sort()
        return -pq[k-1]
