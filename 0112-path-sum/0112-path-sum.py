# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def toPath(root,target):
            if not root:
                return False
            if not root.left and not root.right:
                return target == root.val
            if toPath(root.right,target = target - root.val):
                return True
            if toPath(root.left,target = target - root.val):
                return True
            return False
        return toPath(root,targetSum)