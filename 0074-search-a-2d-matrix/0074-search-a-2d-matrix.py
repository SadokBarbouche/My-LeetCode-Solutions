class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        expanded = []
        for row in matrix:
            expanded.extend(row)
        
        low = 0
        high = len(expanded) - 1
        while low <= high:
            mid = (low + high)
            if expanded[mid] > target:
                high = mid - 1
            elif expanded[mid] < target:
                low = mid + 1
            else:
                return True
        
        return False