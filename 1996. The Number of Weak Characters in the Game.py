class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        res = 0
        max_defense = 0
        properties.sort(key = lambda x: (x[0], -x[1]))
        
        print(properties)
        
        for _, defense in reversed(properties):
            if defense < max_defense:
                res += 1
            else:
                max_defense = defense
                
        return res