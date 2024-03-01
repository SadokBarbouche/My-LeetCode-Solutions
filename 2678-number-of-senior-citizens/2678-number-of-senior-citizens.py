class Solution:
    def countSeniors(self, details: List[str]) -> int:
        ans = 0
        for detail in details:
            ans += int(detail[11:13]) > 60
        return ans