# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:

        # Find the total sum first
        def dfs(node):
            if node == None:
                return 0
            return (node.val + dfs(node.left) + dfs(node.right))

        total = dfs(root)

        # DFS to obtain the maximum product 
        self.ans = 0 
        def dfs(root):
            if root == None: 
                return 0
            currSum = dfs(root.left) + dfs(root.right) + root.val
            self.ans = max(self.ans, currSum * (total - currSum))
            return currSum

        dfs(root)
        
        return self.ans % (10**9+7)
