class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        diff = 1e6
        arr.sort()
        z = zip(arr, arr[1:])
        for i, j in z:
            if j - i < diff:
                diff = j - i
        z = list(zip(arr, arr[1:]))
        ans = []
        for i, j in z:
            if j - i == diff:
                ans.append([i, j])
        return ans
