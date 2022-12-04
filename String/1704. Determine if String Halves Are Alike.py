class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        
        a_cnt , b_cnt = 0, 0
        a = s[:len(s)//2]
        b = s[len(s)//2:]
        
        for i in a:
            if i in vowels:
                a_cnt += 1
    
        for j in b:
            if j in vowels:
                b_cnt += 1
                
        return a_cnt == b_cnt
