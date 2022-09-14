# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        dic = defaultdict(int)
        res = [0]
        
        def dfs(node, dic):
            if node is None:
                return 
            dic[str(node.val)] += 1
            
            if node.left is None and node.right is None:
                odd = 0
                for i in dic:
                    if dic[i] % 2 != 0:
                        odd+=1
                if odd<=1:
                    res[0] += 1
            dfs(node.left, dic)
            dfs(node.right, dic)
            dic[str(node.val)] -= 1
            
        dfs(root, dic)
        return res[0]
