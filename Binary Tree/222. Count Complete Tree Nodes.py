class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        
        # If depth of left subtree == depth of right subtree: left subtree has to be a complete BS
        # If !=: right subtree has to be the one with a complete BS 
        
        def depth(node):
            if not node:
                return 0 
            return 1 + depth(node.left)
        
        def main(node):
            if not node:
                return 0
            
            left = depth(node.left)
            right = depth(node.right)
            print(left,right)
            
            if left == right:
                return pow(2,left) + main(node.right)
            else:
                return pow(2,right) + main(node.left)
            
        return main(root)  
                
        """
        # O(N) TC DFS Approach
        res = [0]
        
        def dfs(node):
            if not node:
                return 
            res[0]+=1
            if node.left:
                dfs(node.left)
            if node.right:
                dfs(node.right)
                
        dfs(root)
        return res[0]"""
