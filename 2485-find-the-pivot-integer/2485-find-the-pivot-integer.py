class Solution:
    def pivotInteger(self, n: int) -> int:
        total_sum = n * (n + 1) // 2
        left_sum = 0
        for i in range(1, n + 1):
            if left_sum == total_sum - left_sum - i:
                return i
            left_sum += i
        return -1
