class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        alpha = set() 
        
        for letter in sentence:
            if ord(letter) in alpha:
                continue
            else:
                alpha.add(ord(letter))
        
        if len(alpha) != 26:
            return False
        else:
            return True
