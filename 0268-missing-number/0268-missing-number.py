class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        s = set()
        n = len(nums)
        for i in nums:
            s.add(i)
        s = list(s)
        for i in range(n):
            if s[i] != i:
                return i
        return n