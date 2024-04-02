class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        ans = 0
        temp_word = word
        while temp_word in sequence:
            temp_word += word
            ans += 1
        return ans
