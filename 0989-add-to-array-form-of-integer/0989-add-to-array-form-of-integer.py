class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        to_add = 0
        for i in range(len(num)):
            to_add += num[len(num)-i-1] * 10 ** i
        s = str (to_add + k)
        ans = []
        for i in s:
            ans.append(int(i))
        return ans