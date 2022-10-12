class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        
        for i in range(len(nums)-3, -1, -1): # Triangle Inequality Theorem
            if nums[i] + nums[i+1] > nums[i+2]:
                return sum(nums[i:i+3])
              
        return 0
