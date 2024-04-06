class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        pascal = []
        for i in range(numRows):
            row = [None] * (i + 1)
            row[0] = 1
            for j in range(1, i):
                row[j] = pascal[i-1][j-1] + pascal[i-1][j]
            row[-1] = 1
            pascal.append(row)
        return pascal