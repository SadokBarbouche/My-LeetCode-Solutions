class Solution:
    def incremovableSubarrayCount(self, nums: List[int]) -> int:
        ans = 0
        for i in range(len(nums)):
            for j in range(i+1, len(nums)+1):
                check = nums[:i] + nums[j:]
                test = sorted(check)
                if test == check and len(set(check)) == len(check) :
                    ans += 1
        return ans