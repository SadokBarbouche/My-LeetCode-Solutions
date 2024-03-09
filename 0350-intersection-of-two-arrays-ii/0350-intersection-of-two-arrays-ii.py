class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        occ_num1 , occ_num2 = dict() , dict()
        for num in nums1:
            if num in occ_num1:
                occ_num1[num] += 1
            else:
                occ_num1[num] = 1
        for num in nums2:
            if num in occ_num2:
                occ_num2[num] += 1
            else:
                occ_num2[num] = 1

        inter = set(nums1).intersection(set(nums2))
        ans = []
        for i in inter:
            freq = min(occ_num1[i], occ_num2[i])
            for _ in range(freq):
                ans.append(i)
        return ans
