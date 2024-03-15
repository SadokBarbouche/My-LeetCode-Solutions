class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        zero_count = 0
        total_product = 1
        ans = [0] * n

        for num in nums:
            if num == 0:
                zero_count += 1
            else:
                total_product *= num

        if zero_count > 1:
            return ans
        elif zero_count == 1:
            for i in range(n):
                if nums[i] == 0:
                    ans[i] = total_product
        else:
            for i in range(n):
                ans[i] = total_product // nums[i]

        return ans
