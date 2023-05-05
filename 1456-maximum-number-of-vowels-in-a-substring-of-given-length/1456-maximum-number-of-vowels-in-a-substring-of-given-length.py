class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set(['a', 'e', 'i', 'o', 'u'])
        ans = 0
        count = 0
        for i in range(len(s)):
            if i >= k and s[i-k] in vowels:
                count -= 1
            if s[i] in vowels:
                count += 1
            ans = max(ans, count)
        return ans
