class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        freq = {i:0 for i in nums}
        for i in nums:
            freq[i]+=1
        for i in freq.values():
            if i > 1:
                return True
        return False