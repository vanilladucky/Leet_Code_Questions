# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.res = root.val

        def dfs(node):
            if not node:
                return 0

            left_max = dfs(node.left)
            right_max = dfs(node.right)
            
            left_max = max(left_max,0)
            right_max = max(right_max,0)

            self.res = max(self.res, node.val+left_max+right_max)
            
            return max(node.val+right_max,node.val+left_max)

        dfs(root)
        return self.res
