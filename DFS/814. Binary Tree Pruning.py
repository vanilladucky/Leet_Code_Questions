# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        if not root: # Terminating Condition
            return None
        
        root.left = self.pruneTree(root.left) # Operations
        root.right = self.pruneTree(root.right)
        
        return root if (root.val or root.left or root.right) else None # Call to recursion
