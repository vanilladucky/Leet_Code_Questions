# https://leetcode.com/problems/maximum-69-number/

class Solution:
    def maximum69Number (self, num: int) -> int:
        if len(str(num)) - len(str(num+1)) == -1:
            return num
        string_num = str(num)
        res = ""
        
        for i in range(len(string_num)):
            if string_num[i] == '6':
                break 
                
        res = string_num[:i] + '9' + string_num[i+1:]
        res = "".join(res)
        
        return int(res)
