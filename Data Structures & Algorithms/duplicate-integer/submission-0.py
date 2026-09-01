class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        num_count = {}

        for num in nums:
            num_count[num] = num_count.get(num, 0) + 1
            if num_count[num] > 1:
                return True
        
        return False

        

        