# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        def dfs(one, two):
            if not one and not two:
                return True
            if one and two and one.val == two.val:
                return dfs(one.left, two.left) and dfs(one.right,two.right)
            else:
                return False 

        return dfs(p,q)
