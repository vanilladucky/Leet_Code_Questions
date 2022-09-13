class Solution:
    def minFlips(self, target: str) -> int:
        start = 0 
        flipped = 0 # res
        
        for i in range(len(target)):
            if int(target[i]) != int(flipped%2):
                flipped+=1 
                
        return flipped   
    
# This solution is a O(N) time complexity solution. 
# It may look really confusing at first but the idea behind it is simple.
# We are going to iterate through the target and compare it to each of the corresponding letter of the string 's' 
# But here I didn't create a new string 's' because if I do so, I would have to iterate through the string 's' itself to flip all of the remaining strings. 
# Therefore I will not be creating the string 's' but instead substituting it with flipped%2 variable. 
# What that mean is that when I flip the string even number of times, it would just be zero like what flipped % 2 would give us.
# On the other hand, flipping it odd number of times would give us 1 just like what flipped % 2 would give us.
# Therefore whenever the corresponding strings are not equal to each other, I would have to flip the string once more and would add 1 to the flipped variable. 
# In the end, returning the variable flipped would do the job!
