class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        sortedArr = [0,0,0]
        for i in nums:
            sortedArr[i] += 1
            
        ptr = 0
        for j in range(len(sortedArr)):
            for i in range(sortedArr[j]):
                nums[ptr] = j
                ptr += 1