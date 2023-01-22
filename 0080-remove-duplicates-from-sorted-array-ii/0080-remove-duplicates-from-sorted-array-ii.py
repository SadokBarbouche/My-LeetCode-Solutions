class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        for element in nums:
            while nums.count(element) > 2:
                nums.remove(element)
        return len(nums)