class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        nums_dict = Counter(nums)
        for k, v in nums_dict.items():
            if v > 1:
                return True

        return False