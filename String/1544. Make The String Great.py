class Solution:
    def makeGood(self, s: str) -> str:
        for i in range(len(s)-1):
            # 97 and 65; 97-65 = 32 - ASCII code
            if abs(ord(s[i])-ord(s[i+1])) == 32:
                return self.makeGood(s[:i]+s[i+2:])
            
        return s
