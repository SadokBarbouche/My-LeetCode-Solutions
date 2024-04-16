class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1:
            new_node = TreeNode(val)
            new_node.left = root
            return new_node

        def dfs(node, curr_depth):
            if not node:
                return

            if curr_depth == depth - 1:
                new_node_left = TreeNode(val)
                new_node_right = TreeNode(val)
                new_node_left.left = node.left
                new_node_right.right = node.right
                node.left = new_node_left
                node.right = new_node_right
                return

            dfs(node.left, curr_depth + 1)
            dfs(node.right, curr_depth + 1)

        dfs(root, 1)
        return root
