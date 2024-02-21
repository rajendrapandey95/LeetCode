class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        # Initialize a variable to count the number of shifts
        shift = 0
        
        # Shift `left` and `right` to the right until they are equal
        while left < right:
            left >>= 1
            right >>= 1
            shift += 1
        
        # Shift `left` (or `right` as both are equal now) back to the left
        # by the number of shifts to get the common prefix followed by zeros
        return left << shift
