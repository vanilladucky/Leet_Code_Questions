class Solution:
    def frequencySort(self, s: str) -> str:
        freq = defaultdict(int)
        res = ""
        
        for c in s:
            freq[c] += 1
            
        sorted_freq = dict(sorted(freq.items(), key=lambda item: -1*item[1]))
        
        for c in sorted_freq:
            res += (c*sorted_freq[c])
            
        return res
