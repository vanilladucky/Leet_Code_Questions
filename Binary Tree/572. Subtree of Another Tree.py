# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sametree(self, one, two):
        if not one and not two:
            return True
        if one and two and one.val == two.val:
            return self.sametree(one.left,two.left) and self.sametree(one.right,two.right)
        return False

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root: # If reached end of the root, it's false 
            return False
        if not subRoot: # Checking for default empty subRoots
            return True

        if self.sametree(root, subRoot):
            return True
        else:
            return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
