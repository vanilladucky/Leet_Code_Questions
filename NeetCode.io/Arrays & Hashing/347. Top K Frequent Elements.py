# https://leetcode.com/problems/top-k-frequent-elements/

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        
        for i in nums:
            count[i]+=1
            
        count = sorted(count.items(), key=lambda item: -1*item[1])
        res = []
        
        tmp = 0 
        for item in count:
            if tmp < k:
                res.append(item[0])
                tmp+=1
                
        return res
