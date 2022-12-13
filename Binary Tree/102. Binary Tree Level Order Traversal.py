# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
            
        res = []
        queue = [root]

        while queue:
            level_values = []
            queue_len = len(queue)

            for i in range(queue_len):
                node = queue.pop(0)
                if node:
                    level_values.append(node.val)
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)

            res.append(level_values)

        return res
