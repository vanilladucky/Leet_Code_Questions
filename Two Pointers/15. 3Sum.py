class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for x in range(len(nums)-2):
            if x>=1 and nums[x] == nums[x-1]:
                continue
            left, right = x+1, len(nums)-1
            while left < right:
                curr = nums[x] + nums[left] + nums[right]
                if curr == 0:
                    res.append([nums[x], nums[left], nums[right]])
                    while left < right and nums[left]==nums[left+1]:
                        left += 1
                    while left < right and nums[right] == nums[right-1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif curr > 0:
                    right -= 1
                else:
                    left += 1
