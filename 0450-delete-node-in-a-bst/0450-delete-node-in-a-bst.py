# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        # Look for the node
        # Check whether it has no or one child
        #   If so : remove it
        # If it has 2 children
        #   Remove it by replacing it with the minimum
        
        def minimumNode(root):
            curr = root
            ans = 0
            while curr and curr.left:
                curr = curr.left
            return curr

        if not root:
            return None
        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            else:
                minNode = minimumNode(root.right)
                root.val = minNode.val
                root.right = self.deleteNode(root.right, minNode.val)
        return root