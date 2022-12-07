class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        res = [0]

        def dfs(node):
            if node:
                if low <= node.val <= high:
                    res[0]+=node.val
                if low < node.val:
                    dfs(node.left)
                if node.val < high:
                    dfs(node.right)

        dfs(root)
        return res[0]
