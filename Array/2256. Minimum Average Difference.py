class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        left,right,mins,n = 0 , sum(nums), float('inf'),len(nums)
        
        for i in range(n):
            left += nums[i]
            right-= nums[i]
            first = left//(i+1) 
            second = 0 if i+1 ==n else right//(len(nums)-(i+1))
            
            result = abs(first - second)
            
            if(result<mins):
                mins=result
                res=i
        return res
