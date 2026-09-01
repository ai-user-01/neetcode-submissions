class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        nums1_dict = set(nums1)
        nums2_dict = set(nums2)
        nums1_unique = list(nums1_dict - nums2_dict)
        nums2_unique = list(nums2_dict - nums1_dict)
        return [nums1_unique, nums2_unique]