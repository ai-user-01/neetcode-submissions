class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        if len(nums) < 2:
            return False

        nums_count = {}
        for num in nums:
            nums_count[num] = 1 + nums_count.get(num, 0)

            if nums_count[num] > 1:
                return True

        return False

        