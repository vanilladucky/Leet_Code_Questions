class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        correct = { '(':')', '{':'}', '[':']' }
        
        for char in s:
            if stack and stack[-1] in correct and correct[stack[-1]] == char:
                stack.pop()
            else:
                stack.append(char)
        
        return False if stack else True
