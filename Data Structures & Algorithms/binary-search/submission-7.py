class Solution:
    def search(self, nums: List[int], t: int) -> int:

        l, r = 0, len(nums)-1
        while l <= r:				# <= 	--for 1 ele arr eg [5]
            mid = l + ((r-l) // 2)		# m = l + ((r-l) // 2) to avoid overflow if
            if nums[mid] < t:			# both l & r are 2^31 size int in java lan			
                l = mid+1			# this avoid adding two big ints & causing overflow error
            elif nums[mid] > t:
                r = mid-1
            else:
                return mid

        return -1   
