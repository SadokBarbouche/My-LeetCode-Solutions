# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        return self.findLCA(root, p, q)
    
    def findLCA(self, root, p, q):
        if root is None:
            return None
        
        if (p.val < root.val and q.val > root.val) or (q.val < root.val and p.val > root.val):
            return root
        
        if p.val == root.val:
            return p
        if q.val == root.val:
            return q
        
        if p.val < root.val:
            return self.findLCA(root.left, p, q)
        else:
            return self.findLCA(root.right, p, q)
