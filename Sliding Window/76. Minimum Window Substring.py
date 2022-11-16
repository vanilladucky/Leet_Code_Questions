class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        
        t_dict = defaultdict(int)
        for c in t:
            t_dict[c]+=1
            
        required = len(t_dict)
        formed = 0
        
        s_dict = defaultdict(int)
        
        res, resLen = [-1, -1], float("infinity")
        left = 0
        
        for right in range(len(s)):
            c = s[right]
            
            if c in t_dict:
                s_dict[c] += 1
                
            if c in t_dict and s_dict[c] == t_dict[c]:
                formed+=1
                
            while formed == required:
                if (right-left+1) < resLen:
                    res = [left,right]
                    resLen = right-left+1
                          
                l = s[left]
                if l in t_dict:
                    s_dict[l] -= 1
                
                if l in t_dict and s_dict[l] < t_dict[l]:
                    formed-=1
                
                left+=1
                
        l, r = res
        return s[l:r+1] if resLen != float('infinity') else ""
