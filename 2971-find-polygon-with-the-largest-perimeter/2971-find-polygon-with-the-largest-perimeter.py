class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        s = 0
        ans = -1
        for num in nums:
            if num < s:
                ans = num + s
            s += num
        return ans