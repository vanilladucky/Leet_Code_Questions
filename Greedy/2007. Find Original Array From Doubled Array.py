class Solution:
    def findOriginalArray(self, nums: List[int]) -> List[int]:
        ans = [] 
        vacans = [] 
        if len(nums)%2:
            return ans    
        nums.sort()
        temp = Counter(nums)        
        for i in nums:
            if temp[i] == 0:
                continue
            else:
                if temp.get(i*2, 0) >= 1:
                    ans.append(i)
                    temp[i] -= 1
                    temp[i*2] -= 1
                else:
                    return vacans
        return ans
