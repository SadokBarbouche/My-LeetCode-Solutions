class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        freq = {i:0 for i in nums}
        for i in nums:
            freq[i]+=1
        for i in nums:
            if freq[i]>1:
                return i
        return -1