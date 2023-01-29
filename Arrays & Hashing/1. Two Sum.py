# https://leetcode.com/problems/two-sum/

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index_dict = collections.defaultdict(list)
        for i in range(len(nums)):
            index_dict[nums[i]].append(i)
            
        res = []
        
        for i in range(len(nums)):
            if target-nums[i] in index_dict:
                if target-nums[i] != nums[i]:
                    res.append(i)
                    res.append(index_dict[target-nums[i]][0])
                    return res
                else:
                    if len(index_dict[target-nums[i]]) >= 2:
                        res.append(i)
                        res.append(index_dict[target-nums[i]][1])
                        return res
                    else:
                        continue
