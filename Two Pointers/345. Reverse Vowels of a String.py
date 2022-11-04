class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)
        vowels = ['a','e','i','o','u','A','E','I','O','U']
        left, right = 0, len(s)-1
        while (left<=right):
            if (s[left] in vowels and s[right] in vowels):
                s[left], s[right] = s[right], s[left]
                left+=1
                right-=1
            elif (s[left] in vowels and s[right] not in vowels):
                right-=1
            elif (s[left] not in vowels and s[right] in vowels):
                left+=1
            else:
                right-=1
                left+=1
        return ''.join([str(elem) for elem in s])
