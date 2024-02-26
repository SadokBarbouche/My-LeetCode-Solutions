class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1.extend(nums2)
        nums1.sort()
        size = len(nums1)
        mid = size // 2
        if size % 2 == 1:
            return nums1[mid]
        else:
            return (nums1[mid] + nums1[mid-1]) / 2
