class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        counter = dict()
        for i in nums:
            if i in counter:
                counter[i]+=1
            else:
                counter[i]=1
        
        for i in nums:
            if counter[i]>1:
                return i
        return -1