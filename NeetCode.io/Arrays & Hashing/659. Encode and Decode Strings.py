"""
Design an algorithm to encode a list of strings to a string. 
The encoded string is then sent over the network and decoded back to the original list of strings
"""

class Solution:
    def encode(self, list_of_strings) -> str:
        res = ""
        for s in list_of_strings:
            res += (str(len(s)) + "#" + s)
        return res

    def decode(self, s) -> list :
        res, i = [], 0

        while i < len(s):
            if s[i] == "#":
                count = s[i-1]
                res.append(s[i+1:i+1+int(count)])
                i+=int(count)
            else:
                i+=1

        return res
