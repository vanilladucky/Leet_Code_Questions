# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        
        def dfs(node, path, summ, res):
            if not node:
                return 
 
            path.append(node.val)
            
            if not node.left and not node.right and summ==targetSum-node.val: # Leaf
                res.append(list(path))
            
            dfs(node.left, path, summ+node.val, res)
            dfs(node.right, path, summ+node.val, res)
            
            path.pop()
             
        res = []
        dfs(root, [], 0, res)
        return res
