class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def countK(nums: List[int], k: int) -> int:
            counter = collections.Counter()
            left = 0
            distinct_count = 0
            result = 0

            for right, num in enumerate(nums):
                if counter[num] == 0:
                    distinct_count += 1
                counter[num] += 1

                while distinct_count > k:
                    counter[nums[left]] -= 1
                    if counter[nums[left]] == 0:
                        distinct_count -= 1
                    left += 1

                result += right - left + 1

            return result

        return countK(nums, k) - countK(nums, k - 1)