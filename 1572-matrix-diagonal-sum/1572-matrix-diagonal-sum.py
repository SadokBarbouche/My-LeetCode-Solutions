class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        fd,sd = 0,0
        mid = len(mat) // 2
        for i in range(len(mat)):
            fd += mat[i][i]
            sd += mat[i][len(mat)-i-1]
        return fd+sd - mat[mid][mid] if len(mat) % 2 == 1 else fd+sd