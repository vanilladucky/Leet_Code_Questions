# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution: # O(N)
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def dfs(node):
            if not node: # End Condition
                return False
            
            left = dfs(node.left) # Operations start
            right = dfs(node.right)
            
            if not left:
                node.left = None
            if not right:
                node.right = None # Operations end
                
            return node.val or left or right # Call to Recursion
        
        return root if dfs(root) else None
