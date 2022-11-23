class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        left,right = 0, len(nums)-1
        
        while left<=right:
            mid = (left+right)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid+1
            else:
                right = mid-1
                
        return -1 
      
      
# Recursion 

class Solution:
    def search(self, nums: List[int], target: int) -> int:
      
        def bs(left, right):
            if left <= right:
                mid = (left+right)//2
                if nums[mid] == target:
                    return mid
                elif nums[mid] < target:
                    left = mid+1
                    return bs(left, right)
                else:
                    right = mid-1 
                    return bs(left,right)
            else:
                return -1
            
        return bs(0,len(nums)-1)
