class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        if 1 in nums:
            return False
        nums = list(set(nums))
        len_nums = len(nums)
        nums = sorted(nums)

        for i in range(len_nums - 1):
            for j in range(i + 1, len_nums):
                if gcd(nums[i], nums[j]) > 1:
                    nums[j] *= nums[i]
                    break  
            else:
                return False
        return True