class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        total = 0
        prefix_sum = {0:-1}

        for i, n in enumerate(nums):
            total += n
            r = total % k

            if r not in prefix_sum:
                prefix_sum[r] = i
            elif i - prefix_sum[r] > 1:
                return True

        return False



            