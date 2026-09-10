class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        L, R, res = [0]*n, [0]*n, [0]*n

        L[0], R[len(res)-1] = 1, 1

        for i in range(1, len(nums)):
            L[i] = nums[i-1] * L[i-1]

        for i in range(len(nums)-2, -1, -1):
            R[i] = nums[i+1] * R[i+1]
        
        for i in range(len(nums)):
            res[i] = L[i] * R[i]

        return res

        