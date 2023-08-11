class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        subset = []
        def dfs(index,nums):
            if index >= len(nums):
                ans.append(subset[:])
                return
            subset.append(nums[index])
            dfs(index+1,nums)
            subset.pop()
            dfs(index+1,nums)
        
        dfs(0,nums)
        return ans
            