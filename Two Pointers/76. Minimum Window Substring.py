class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""
        
        dict_t = Counter(t)
        total_length = len(dict_t)
        
        l, r = 0, 0
        
        matched = 0 
        
        window_count = defaultdict(int)
        
        res = (float('inf'), None, None)
        
        while r < len(s):
            char = s[r]
            window_count[char] += 1
            
            if char in dict_t and window_count[char] == dict_t[char]:
                matched += 1
                
            # Moving the left pointer
            while l <= r and matched == total_length:
                char = s[l]
                
                if r-l+1 < res[0]:
                    res = (r-l+1, l, r)
                    
                window_count[char] -= 1
                if char in dict_t and window_count[char] < dict_t[char]:
                    matched -= 1
                    
                l += 1
            # Finished moving the left pointer 
            
            # Moving the right pointer
            r += 1
            
        return "" if res[0] == float('inf') else s[res[1]: res[-1]+1]
