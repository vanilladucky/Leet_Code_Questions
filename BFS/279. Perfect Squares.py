class Solution:
    def numSquares(self,n):
        squares = [i**2 for i in range(1, int(n**0.5)+1)] # Creating all possible values of the perfect squares 
        f_lvl, s_lvl, depth = {n}, set(), 1
        
        while f_lvl:
            for node in f_lvl:
                for square in squares: # Check against all squares 
                    if square == node:
                        return depth
                    if square > node: # If the square is bigger than the number, no point in checking
                        break
                    s_lvl.add(node-square) # Add the difference to the next level 
            f_lvl, s_lvl, depth = s_lvl, set(), depth+1 # Keep continuing on 
