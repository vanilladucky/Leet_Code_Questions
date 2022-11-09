class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0]*len(temperatures)
        stack = []
        
        for i in range(len(temperatures)):
            while stack and temperatures[i] > stack[-1][1]:
                tmp = stack.pop()
                index, val = tmp[0], tmp[1] 
                res[index] = i-index
            stack.append([i,temperatures[i]])
            
        return res
