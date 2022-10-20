class Solution:
    def intToRoman(self, num: int) -> str:
        res = ""
        dic={1:'I',5:'V',10:'X',50:'L',100:'C',500:'D',1000:'M'}
        i = 1
        
        while num != 0:
            y = num % 10
            num = num // 10 
            if y == 5:
                res = dic[y * (10**(i-1))] + res
            elif y == 1:
                res = dic[y * (10**(i-1))] + res
            elif y == 4:
                res = dic[1*(10**(i-1))] + dic[5*(10**(i-1))] + res
            elif y == 9:
                res = dic[1*(10**(i-1))] + dic[1*(10**i)] + res
            elif y < 4:
                res = dic[1*(10**(i-1))] * y + res
            elif y < 9:
                res = dic[5*(10**(i-1))] + dic[1*(10**(i-1))] * (y-5) + res
            i+=1
        
        return res
