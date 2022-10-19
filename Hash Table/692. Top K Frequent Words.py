class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        hashmap = defaultdict(int)
        for word in words:
            hashmap[word] += 1
        
        arr = []
        for i in hashmap:
            arr.append([hashmap[i], i])
            
        arr.sort(key=lambda x: (1/x[0], x[1]))
        
        res = []
        for i in range(k):
            res.append(arr[i][1])
            
        return res
