from typing import List

class Solution:
    """
    Solution class to create a 2D array from a given integer array with distinct integers in each row.
    """

    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        """
        Create a 2D array from the given integer array satisfying specified conditions.

        Parameters:
        - nums (List[int]): The input integer array.

        Returns:
        - List[List[int]]: The resulting 2D array.

        Constraints:
        - 1 <= len(nums) <= 200
        - 1 <= nums[i] <= len(nums)
        """

        # Initialize a frequency array to keep track of the count of each integer.
        freq = [0] * (len(nums) + 1)

        # Initialize the result 2D array.
        ans = []

        for c in nums:
            # Check if the frequency of the current integer requires a new row.
            if freq[c] >= len(ans):
                ans.append([])

            # Store the integer in the list corresponding to its current frequency.
            ans[freq[c]].append(c)
            
            # Increment the frequency count of the current integer.
            freq[c] += 1

        return ans
