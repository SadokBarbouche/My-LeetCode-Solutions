# # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True

        queue = deque([root])
        depth = 0
        
        while queue:
            prev = None
            for i in range(len(queue)):
                node = queue.popleft()
                
                if depth % 2 == 0:
                    if node.val % 2 == 0:
                        return False
                    if prev is not None and prev >= node.val:
                        return False
                else: 
                    if node.val % 2 != 0:
                        return False
                    if prev is not None and prev <= node.val:
                        return False
                prev = node.val
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            depth += 1
            
        return True
