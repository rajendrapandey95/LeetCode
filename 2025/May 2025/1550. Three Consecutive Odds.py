class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        return any(arr[i]%2 and arr[i+1]%2 and arr[i+2]%2 for i in range(len(arr)-2))
