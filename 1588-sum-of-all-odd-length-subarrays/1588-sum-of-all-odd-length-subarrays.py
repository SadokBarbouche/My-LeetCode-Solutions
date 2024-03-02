class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        s = 0
        pf = []
        for i in arr:
            s += i
            pf.append(s)
        ans = sum(arr)
        n = len(arr)
        
        for length in range(3, n + 1, 2):
            for i in range(n - length + 1):
                j = i + length - 1
                if i == 0:
                    ans += pf[j]
                else:
                    ans += pf[j] - pf[i - 1]
                    
        return ans
