class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        str1, str2 = "", ""
        
        for i in word1:
            str1 += i
        for j in word2:
            str2 += j
            
        return str1 == str2
