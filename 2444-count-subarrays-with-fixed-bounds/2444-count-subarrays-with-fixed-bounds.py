class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        ans = 0
        minimum = -1
        maximum = -1
        nonelement =-1
        for ind, val in enumerate(nums):
            if val == minK:
                minimum = ind
            if val == maxK:
                maximum = ind
            if not minK<= val <= maxK :
                nonelement = ind
            ans += max(0, min(minimum, maximum) - nonelement)
        return ans