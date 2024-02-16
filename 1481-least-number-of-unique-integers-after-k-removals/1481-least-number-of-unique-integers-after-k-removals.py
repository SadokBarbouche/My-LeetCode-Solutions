class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        num2occ = {}
        for num in arr:
            if num in num2occ:
                num2occ[num] += 1
            else:
                num2occ[num] = 1

        sorted_occurrences = sorted(num2occ.values())
        unique_ints_removed = 0

        for occ in sorted_occurrences:
            if k >= occ:
                k -= occ
                unique_ints_removed += 1
            else:
                break

        return len(num2occ) - unique_ints_removed
