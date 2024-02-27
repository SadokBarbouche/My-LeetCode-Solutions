# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return 0, 0
            left_depth, left_diameter = dfs(node.left)
            right_depth, right_diameter = dfs(node.right)
            current_depth = max(left_depth, right_depth) + 1
            current_diameter = max(left_depth + right_depth, left_diameter, right_diameter)
            return current_depth, current_diameter
        
        _, diameter = dfs(root)
        return diameter
