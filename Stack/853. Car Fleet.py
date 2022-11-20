class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        tmp = [(pos,speed) for pos, speed in zip(position,speed)]
        tmp.sort(reverse=True)
        stack = []
        
        for pair in tmp:
            stack.append((target-pair[0])/pair[1]) # Hour taken to reach destination
            if len(stack) >= 2 and stack[-1]<=stack[-2]: 
              """Here we check whether this pair is capable of catching up with the car that started ahead of it - if it is capable of catching up, 
              it is to be classified as a 'car fleet' along with the car ahead of it so it gets removed from the stack to prevent counting duplicates"""
                stack.pop()
                
        return len(stack) # Stack would only contain the first cars in their respective car fleets 
