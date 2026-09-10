class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        res = 0

        for n in nums_set:
            if n-1 not in nums_set:
                local_res = 0
            
                while n+local_res in nums_set:
                    local_res += 1

                res = max(res, local_res)

        return res


