class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        nums = [num for row in grid for num in row]
        nums.sort()
        n = len(nums)
        operations = 0
        median = nums[n // 2]
        for num in nums:
            diff = abs(num - median)
            if diff % x != 0:
                return -1
            operations += diff // x

        return operations