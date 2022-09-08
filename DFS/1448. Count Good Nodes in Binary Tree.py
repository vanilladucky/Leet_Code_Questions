# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        res = [0]
        
        def good(node, maxsofar):
            if not node:
                return
            
            if node.val >= maxsofar:
                res[0] += 1
                maxsofar = node.val
                
            good(node.left, maxsofar)
            good(node.right, maxsofar)
        
        good(root, root.val)
        
        return res[0]