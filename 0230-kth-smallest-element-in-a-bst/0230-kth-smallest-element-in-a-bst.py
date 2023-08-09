class Solution:
    
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def inorderTraversal(root,traversal=[]):
            if not root:
                return
            inorderTraversal(root.left,traversal)
            traversal.append(root.val)
            inorderTraversal(root.right,traversal)
            return traversal
        
        traversal = inorderTraversal(root)
        return traversal[k-1]