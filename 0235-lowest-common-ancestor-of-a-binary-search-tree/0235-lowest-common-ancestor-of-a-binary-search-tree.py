# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def search(root, val):
            if root is None: 
                return None
            
            if val > root.val:
                return search(root.right, val)
            elif val < root.val:
                return search(root.left, val)
            else:
                return root
        
        search_p, parent_p = search(root, p.val), None
        search_q, parent_q = search(root, q.val), None
        
        if search_p is None or search_q is None:
            return None
        
        return self.findLCA(root, search_p, search_q)
    
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
