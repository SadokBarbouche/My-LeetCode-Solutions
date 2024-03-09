class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        set1,set2 = set(nums1),set(nums2)
        common_elements = list(set1.intersection(set2))
        return min(common_elements) if common_elements else -1
