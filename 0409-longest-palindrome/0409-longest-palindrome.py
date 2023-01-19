class Solution:
    def longestPalindrome(self, s: str) -> int:
        ans = 0
        found_impair = False
        freq = {i:0 for i in s}
        for i in s:
            freq[i]+=1
        sorted_freq = [i for i in freq.values()]
        for freq in sorted_freq:
            if freq%2 == 0:
                ans += freq
            else:
                found_impair = True
                ans += freq - 1
        return ans+1 if found_impair else ans
    