class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = ['+', '-', '*', '/']
        
        for char in tokens:
            if char not in operators:
                stack.append(int(char))
            else:
                second = stack.pop()
                first = stack.pop()
                
                if char == '+':
                    result = int(first+second)
                elif char == '-':
                    result = int(first-second)
                elif char == '*':
                    result = int(first*second)
                else:
                    result = int(first/second)
                    
                stack.append(result)
                
        return int(stack[0])
