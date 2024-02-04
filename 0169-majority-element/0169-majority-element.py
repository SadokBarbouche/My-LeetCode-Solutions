class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d = dict()
        for i in nums:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        
        argmax = max(d.values())
        for i,j in d.items():
            if j == argmax:
                return i
        return 0