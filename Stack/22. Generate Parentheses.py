class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        
        def backtrack(paran, left, right):
            if len(paran)==2*n:
                res.append(paran)
                return 
            
            if left < n:
                backtrack(paran+'(', left+1, right)
                
            if left > right:
                backtrack(paran+')', left, right+1)
        
        backtrack("", 0, 0)
        return res
        
        """res = []
        
        def isvalid(paran):
            if not paran or paran[0] == '}':
                return False
            stack = []
            dic = {')':'('}
            for i in paran:
                if i in dic and stack and dic[i] == stack[-1]:
                    stack.pop()
                else:
                    stack.append(i)
                    
            return False if stack else True
            
        def backtrack(formation):
            if len(formation) > 2*n:
                return
                
            if len(formation) == 2*n and isvalid(formation):
                res.append(formation)
                return
            
            backtrack(formation+'(')
            backtrack(formation+')')
            
        backtrack("")
        return res"""
