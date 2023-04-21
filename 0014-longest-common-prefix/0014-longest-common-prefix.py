class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        z = zip(*strs)
        ans = ""
        for group in z:
            if len(set(group)) == 1:
                ans += group[0]
            else:
                break
        return ans
