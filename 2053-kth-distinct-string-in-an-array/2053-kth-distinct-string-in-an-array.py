class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        count = dict()
        for i in arr:
            if i in count:
                count[i] += 1
            else:
                count[i] = 1
        
        distinct_count = 0
        for i in arr:
            if count[i] == 1:
                distinct_count += 1
                if distinct_count == k:
                    return i
        return ""
