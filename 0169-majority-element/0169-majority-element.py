class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d = {}
        for i in nums:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        inv_map = {v: k for k, v in d.items()}
        argmax = max(d.values())
        
        return inv_map[argmax]