class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        ans, c = 1, 1
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                c += 1
            else:
                ans,c = max(ans,c),1
        ans,c = max(ans,c),1
        for i in range(len(nums)-1):
            if nums[i] < nums[i+1]:
                c += 1
            else:
                ans,c = max(ans,c),1
        return max(ans,c)    
            
        
                