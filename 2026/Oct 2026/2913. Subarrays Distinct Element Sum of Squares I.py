class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        n, ans=len(nums), 0
        for l in range(n):
            seen, cnt=0, 0
            for x in nums[l:]:
                cnt+=((seen>>x)&1)==0
                seen|=(1<<x)
                ans+=cnt*cnt
        return ans
