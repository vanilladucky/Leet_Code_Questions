class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        occur = defaultdict(int)
        
        for i in arr:
            occur[i] += 1
            
        check = set()
        for value in occur.values():
            if value in check:
                return False
            else:
                check.add(value)
        
        return True
