class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        graph = [0] * (n+1)

        for (a,b) in trust:
            graph[a] -= 1
            graph[b] += 1

        for i in range(1, len(graph)):
            if graph[i] == n-1:
                return i 
        
        return -1 
