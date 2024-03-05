class Solution:
    def minimumLength(self, s: str) -> int:
        left, right = 0, len(s) - 1
        while left < right and s[left] == s[right]:
            curr = s[left]
            while left <= right and s[left] == curr:
                left += 1
            while right >= left and s[right] == curr:
                right -= 1
        return right - left + 1 if left <= right else 0
