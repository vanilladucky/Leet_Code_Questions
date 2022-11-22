class Solution:
    def numSquares(self,n):
        squares = [i**2 for i in range(1, int(n**0.5)+1)]
        f_lvl, s_lvl, depth = {n}, set(), 1
        
        while f_lvl:
            for node in f_lvl:
                for square in squares:
                    if square == node:
                        return depth
                    if square > node:
                        break
                    s_lvl.add(node-square)
            f_lvl, s_lvl, depth = s_lvl, set(), depth+1
