class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        if len(palindrome) == 1:
            return ""
        
        for i in range(len(palindrome)//2):
            if palindrome[i] != "a":
                temp = palindrome[:i] + "a" + palindrome[i+1:]
                return temp
            
        temp = palindrome[:-1] + "b"
        return temp
