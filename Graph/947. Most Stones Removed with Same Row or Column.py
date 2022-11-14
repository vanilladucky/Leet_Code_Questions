class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        
        x_cor = defaultdict(list)
        y_cor = defaultdict(list)
        points = {(i,j) for i,j in stones}
        count = 0
        
        def removenodes(a,b):
            points.discard((a,b))
            
            for y in x_cor[a]:
                if (a,y) in points:
                    removenodes(a,y)
            
            for x in y_cor[b]:
                if (x,b) in points:
                    removenodes(x,b)
                    
        for i,j in stones:
            x_cor[i].append(j)
            y_cor[j].append(i)
            
        for x,y in stones:
            if (x,y) in points:
                removenodes(x,y)
                count+=1
                
        return len(stones)-count
