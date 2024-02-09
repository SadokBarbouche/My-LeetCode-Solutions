class Solution:
    def valid(self,i,j):
        return i%j == 0 or j%i == 0
    
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        if not nums:
            return []

        nums.sort()
        n = len(nums)
        dp = [[] for _ in range(n)]
        dp[0] = [nums[0]]

        for i in range(1, n):
            max_subset = []
            for j in range(i):
                if self.valid(nums[i],nums[j]) and len(dp[j]) > len(max_subset):
                    max_subset = dp[j]
            dp[i] = max_subset + [nums[i]]

        return max(dp, key=len)