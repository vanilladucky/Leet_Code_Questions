# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        def dfs(node):
            if not node:
                return None

            tmp = node.right
            node.right = node.left
            node.left = tmp

            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return root
