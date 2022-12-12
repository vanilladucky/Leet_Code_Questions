# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diam = 0 

        def dfs(node):
            if not node:
                return -1

            left = dfs(node.left)
            right = dfs(node.right)
            diam = 2 + left + right
            self.diam = max(self.diam, diam)

            return 1 + max(left, right)

        dfs(root)
        return self.diam
