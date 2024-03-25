class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        counter = dict()
        ans = []
        for i in nums:
            if i in counter:
                counter[i] += 1
                ans.append(i)
            else:
                counter[i] = 1
        return ans