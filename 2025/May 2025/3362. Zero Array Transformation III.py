from heapq import heappush, heappop

class Solution(object):
    def maxRemoval(self, nums, queries):
        queries.sort(key=lambda x: x[0])
        heap = []
        deltaArray = [0] * (len(nums) + 2)
        operations = 0
        j = 0

        for i in range(len(nums)):
            operations += deltaArray[i]
            while j < len(queries) and queries[j][0] == i:
                heappush(heap, -queries[j][1]) 
                j += 1

            while operations < nums[i] and heap and -heap[0] >= i:
                end = -heappop(heap)
                operations += 1
                deltaArray[end + 1] -= 1  

            if operations < nums[i]:
                return -1 

        return len(heap)
