class Solution:
    def getSum(self, n):
        sum = 0
        for digit in str(n): 
          sum += int(digit)      
        return sum
    
    def makeIntegerBeautiful(self, n: int, target: int) -> int:
        if self.getSum(n) <= target:
            return 0
    
        res = 0
        
        for i in range(len(str(n))+1):
            if self.getSum(n) <= target:
                return res
            number_we_need_to_add = 10-int(str(n)[-1-i])
            temp = number_we_need_to_add*(10**i)
            n = n + temp
            res+=temp
