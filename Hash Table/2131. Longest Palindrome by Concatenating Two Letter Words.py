class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        count = Counter(words)
        res = 0 
        center = False
        for word, count_of_word in count.items():
            if (word[0] == word[1]):
                if (count_of_word%2==0):
                    res+=count_of_word
                else:
                    center=True
                    res+=(count_of_word-1)
            elif word[0] < word[1]:
                res+=2*min(count_of_word, count[word[1]+word[0]])
        if center:
            res+=1
        return res*2
