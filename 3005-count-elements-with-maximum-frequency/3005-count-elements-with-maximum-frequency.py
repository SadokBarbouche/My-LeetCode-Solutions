class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        d = dict()
        m = 0
        count = 0
        for i in nums:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
            if d[i] > m:
                m = d[i]
                count = 1
            elif d[i] == m:
                count += 1

        return count * m
