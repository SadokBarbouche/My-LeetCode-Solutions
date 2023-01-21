class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums)
        i = 0
        for i in range(start,end):
            middle = (end - start )//2
            if nums[i] == target:
                return i
            elif nums[i] < nums[middle]:
                end = middle
            elif nums[i] > nums[middle]:
                start = middle
        return -1