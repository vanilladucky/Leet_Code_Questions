class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(0) # To ensure all the leftover rectangles are accounted for too
        stack = [-1]
        res = 0 
        
        for i in range(len(heights)):
            print(stack)
            while stack and heights[i] < heights[stack[-1]]:
                print(stack)
                height = heights[stack.pop()]
                width = i - stack[-1] - 1
                res = max(res, height*width)
            stack.append(i)
            
        return res
