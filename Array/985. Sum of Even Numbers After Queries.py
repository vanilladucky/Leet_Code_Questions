class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        answer = []
        summation = sum([i for i in nums if i%2==0]) # O(N)
        
        for arr in queries:
            idx = arr[1]
            before = nums[idx]
            after = nums[idx] + arr[0]
            nums[idx] += arr[0]
            
            if before % 2 != 0: # odd
                if after % 2 == 0:
                    summation += after
            else:
                summation -= before
                if after % 2 == 0:
                    summation += after
            
            answer.append(summation)
            
        return answer
