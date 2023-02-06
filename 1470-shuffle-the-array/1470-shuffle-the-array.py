class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        middle = len(nums) // 2
        ans = []
        for i in range(middle):
            ans.append(nums[i])
            ans.append(nums[middle+i])
            
        return ans