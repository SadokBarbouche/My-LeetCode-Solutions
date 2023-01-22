class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        permutations = []
        for i in range(2**n):
            perm = []
            for j in range(n):
                if (i >> j) & 1:
                    perm.append(nums[j])
            permutations.append(perm)
        return permutations