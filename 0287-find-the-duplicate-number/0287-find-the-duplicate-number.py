class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        counter = dict()
        for i in nums:
            if i in counter:
                counter[i]+=1
                return i
            else:
                counter[i]=1
        return -1        
