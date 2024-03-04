class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        ans = 0
        max_score = 0
        left, right = 0, len(tokens) - 1
        
        while left <= right:
            if tokens[left] <= power:
                power -= tokens[left]
                ans += 1
                left += 1
                max_score = max(max_score, ans)
            elif ans > 0:
                power += tokens[right]
                ans -= 1
                right -= 1
            else:
                break
        
        return max_score