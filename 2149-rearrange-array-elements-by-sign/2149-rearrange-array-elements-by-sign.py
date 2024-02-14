class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos, neg = [],[]
        for num in nums:
            if num>0:
                pos.append(num)
            else:
                neg.append(num)
        ans = []
        for i in zip(pos,neg):
            ans.extend(i)
        return ans