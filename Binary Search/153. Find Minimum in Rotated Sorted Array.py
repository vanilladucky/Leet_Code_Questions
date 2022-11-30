class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums)-1 
        curr_min = float('inf')
        
        while left <= right:
            mid = (left+right)//2
            curr_min = min(curr_min, nums[mid])
            
            if nums[mid] < nums[right]: # min is on the left side
                right = mid - 1
            else: # min is on the right side 
                left = mid + 1
                
        return curr_min
