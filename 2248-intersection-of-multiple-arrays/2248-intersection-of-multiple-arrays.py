class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        ans = set(nums[0])
        for num in nums:
            ans = ans.intersection(num)
        return sorted(ans)