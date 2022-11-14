class Solution:
    def reverseWords(self, s: str) -> str:
        res = []
        slow, fast = 0, 0 
        
        mode = 'blank' if s[0] == ' ' else 'word'
        
        while fast < len(s):
            
            if mode=='blank' and s[fast] != ' ':
                slow = fast
                mode = 'word'
            
            elif mode == 'word' and s[fast] == ' ':
                res.append(s[slow:fast])
                slow = fast
                mode = 'blank'
                
            fast += 1
                
        if (tmp:=s[slow:fast]).isalnum():
            res.append(s[slow:fast])
            
        return " ".join(res[::-1])
