class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        remaining_num = {}

        for i, num in enumerate(nums):
            if target - num in remaining_num:
                return [remaining_num[target - num], i]
            
            remaining_num[num] = i
