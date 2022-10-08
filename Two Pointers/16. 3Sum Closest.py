class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        result = nums[0] + nums[1] + nums[2]
        
        for i in range(len(nums)-2):
            ptr1, ptr2 = i+1, len(nums)-1
            
            while (ptr1<ptr2):
                summ = nums[i] + nums[ptr1] + nums[ptr2]
                if summ == target:
                    return summ
                
                if abs(summ - target) < abs(result - target):
                    result = summ
                    
                if summ < target:
                    ptr1 += 1
                elif summ > target:
                    ptr2 -= 1
            
        return result 
