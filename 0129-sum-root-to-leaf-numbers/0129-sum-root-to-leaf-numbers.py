# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    ans = 0
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        if not root: 
            return 0 
         
        self.dfs(root, root.val)
        return self.ans 
    
    def dfs(self, root, cur): 
        if not root.left and not root.right: 
            self.ans += cur 
        
        if root.left: 
            self.dfs(root.left, cur * 10 + root.left.val)
        if root.right: 
            self.dfs(root.right, cur * 10 + root.right.val) 