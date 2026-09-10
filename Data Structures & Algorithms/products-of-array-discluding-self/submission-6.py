class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        l, r, res = [0]*n, [0]*n, [0]*n

        l[0], r[len(nums)-1] = 1, 1

        for i in range(1, len(nums)):
            l[i] = l[i-1] * nums[i-1]

        for i in range(len(nums)-2, -1, -1):
            r[i] = r[i+1] * nums[i+1]

        for i in range(len(nums)):
            res[i] = l[i] * r[i]

        return res