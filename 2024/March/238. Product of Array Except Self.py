from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        # Initialize arrays to store prefix and suffix products
        prefix_products = [1] * n
        suffix_products = [1] * n
        
        # Calculate prefix products
        for i in range(1, n):
            prefix_products[i] = prefix_products[i - 1] * nums[i - 1]
        
        # Calculate suffix products
        for i in range(n - 2, -1, -1):
            suffix_products[i] = suffix_products[i + 1] * nums[i + 1]
        
        # Multiply corresponding prefix and suffix products to get the final answer
        result = [prefix_products[i] * suffix_products[i] for i in range(n)]
        
        return result
