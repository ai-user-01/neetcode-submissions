class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [0]*len(nums)
        l, r = [0]*len(nums), [0]*len(nums)

        l[0], r[len(nums)-1] = 1, 1
        for i in range(1, len(nums)):
            l[i] = nums[i-1] * l[i-1]
        for i in range(len(nums)-2, -1, -1):
            r[i] = nums[i+1] * r[i+1]
        for i in range(len(nums)):
            res[i] = l[i] * r[i]

        return res