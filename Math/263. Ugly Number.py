class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False
        
        prime = [2,3,5]
        
        for p in prime:
            while n%p==0:
                n /= p
        
        return True if n==1 else False
