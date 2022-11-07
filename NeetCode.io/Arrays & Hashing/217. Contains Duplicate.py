# https://leetcode.com/problems/contains-duplicate/

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        duplicates = set()
        for i in nums:
            if i in duplicates:
                return True
            else:  
                duplicates.add(i)
                
        return False
