class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        arr = list(zip(plantTime, growTime))
        arr.sort(key = lambda x : -x[1])
        
        ret = 0
        
        cur = 0
        
        for plant, grow in arr:
            cur += plant
            ret = max(ret, cur + grow)
            
        return ret
        
