class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums_dict = {}
        for n in nums:
            nums_dict[n] = 1 + nums_dict.get(n, 0)

        for k, v in nums_dict.items():
            if v > len(nums) / 2:
                return k
