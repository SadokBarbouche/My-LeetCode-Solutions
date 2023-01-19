class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefix_sums = []
        s = 0
        for i in nums:
            s+=i
            prefix_sums.append(s)
        n = len(prefix_sums)
        if prefix_sums[n-1]-prefix_sums[0]==0:
            return 0
        for i in range(1,n):
            if prefix_sums[i-1]==prefix_sums[n-1] - prefix_sums[i]:
                return i
        return -1