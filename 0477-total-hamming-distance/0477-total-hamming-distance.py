class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        n = len(nums)
        result = 0
        for i in range(32):
            count = 0
            for num in nums:
                count += (num >> i) & 1
            result += count * (n - count)
        return result
