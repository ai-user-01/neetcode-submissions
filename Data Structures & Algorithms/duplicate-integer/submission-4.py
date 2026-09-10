class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums_dict = {}
        for n in nums:
            nums_dict[n] = 1 + nums_dict.get(n, 0)

        for v in nums_dict.values():
            if v > 1:
                return True
        
        return False