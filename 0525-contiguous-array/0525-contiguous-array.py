class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        count = {0: -1}
        curr_count = 0
        max_len = 0

        for i, num in enumerate(nums):
            curr_count += 1 if num == 0 else -1
            if curr_count in count:
                max_len = max(max_len, i - count[curr_count])
            else:
                count[curr_count] = i

        return max_len
