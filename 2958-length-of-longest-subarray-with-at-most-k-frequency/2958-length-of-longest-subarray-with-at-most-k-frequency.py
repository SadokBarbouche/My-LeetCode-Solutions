class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        d = {}
        res = 0
        l = 0

        for r in range(len(nums)):
            d[nums[r]] = d.get(nums[r], 0) + 1
            while d[nums[r]] > k:
                d[nums[l]] -= 1
                l += 1 
            res = max(res, r - l + 1)
        
        return res