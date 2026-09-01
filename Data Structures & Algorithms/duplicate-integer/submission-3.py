class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums_dict = {}
        for n in nums:
            if n in nums_dict:
                return True
            else:
                nums_dict[n] = 1
        return False