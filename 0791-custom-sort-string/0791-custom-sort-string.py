class Solution:
    def customSortString(self, order: str, s: str) -> str:
        counter = Counter(s)
        ans = [c*counter[c] for c in order]
        ans.extend(filter(lambda x: x not in order,s))
        return ''.join(ans)
        