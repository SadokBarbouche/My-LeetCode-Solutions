class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        def largestRectangleArea(heights):
            stack = []
            max_area = 0
            heights.append(0)
            for i in range(len(heights)):
                while stack and heights[i] < heights[stack[-1]]:
                    h = heights[stack.pop()]
                    w = i if not stack else i - stack[-1] - 1
                    max_area = max(max_area, h * w)
                stack.append(i)
            return max_area
        max_area = 0
        heights = [0] * len(matrix[0])
        for row in matrix:
            for i in range(len(row)):
                heights[i] = heights[i] + 1 if row[i] == '1' else 0
            max_area = max(max_area, largestRectangleArea(heights))
        return max_area
