class Solution:
    def minFlips(self, target: str) -> int:
        start = 0 
        flipped = 0 # res
        
        for i in range(len(target)):
            if int(target[i]) != int(flipped%2):
                flipped+=1 
                
        return flipped                