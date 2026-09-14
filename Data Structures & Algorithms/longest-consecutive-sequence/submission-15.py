class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        res = 0

        for i, n in enumerate(nums):
            if n - 1 not in nums_set:
                size = 1
                while n + size in nums_set:
                    size += 1
                
                res = max(res, size)

        return res