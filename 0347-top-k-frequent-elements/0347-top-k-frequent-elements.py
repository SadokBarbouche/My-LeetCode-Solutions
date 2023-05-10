class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        unique = set(nums)
        d = {i:0 for i in unique}
        for i in nums:
            d[i] += 1
        pairs = sorted(d.items(), key=lambda x:x[1],reverse=True)
        ans = []
        for i in range(k):
            ans.append(pairs[i][0])
        return ans